import os
import shutil
import time
import threading
from pathlib import Path
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.text import LabelBase

# === 註冊中文字型（解決 Windows 顯示方框的問題）===
# Windows 系統內建的微軟正黑體路徑
font_path = 'C:/Windows/Fonts/msjh.ttc'
if os.path.exists(font_path):
    LabelBase.register(name='ChineseFont', fn_regular=font_path)
else:
    # 如果在 Linux 或其他環境找不到，使用預設（打包進 Android 時可以放一個 ttf 字型檔案在專案內）
    LabelBase.register(name='ChineseFont', fn_regular='Roboto')

class BackupApp(App):
    def build(self):
        self.title = "自動備份系統"
        
        # 建立簡單的使用者介面
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        self.status_label = Label(
            text="等待插入隨身碟...", 
            font_size=32,
            font_name='ChineseFont',  # 套用中文字型
            halign='center',
            valign='middle'
        )
        self.status_label.bind(size=self.status_label.setter('text_size'))
        
        layout.add_widget(self.status_label)
        
        # 啟動背景監聽執行緒
        self.is_running = True
        self.monitor_thread = threading.Thread(target=self.usb_monitor_loop, daemon=True)
        self.monitor_thread.start()
        
        return layout

    def usb_monitor_loop(self):
        """ 背景持續監聽隨身碟的迴圈 """
        last_processed_usb = None
        
        while self.is_running:
            try:
                storage_dir = Path("/storage")
                found_usb = None
                vehicle_file_path = None
                
                if storage_dir.exists():
                    for item in storage_dir.iterdir():
                        if item.name not in ["emulated", "self", "sdcard0"] and item.is_dir():
                            ru_param = item / "ru_param"
                            ru_logdata = item / "ru_logdata"
                            vehicle_txt = ru_param / "vehicle.txt"
                            
                            if ru_param.is_dir() and ru_logdata.is_dir() and vehicle_txt.exists():
                                found_usb = item
                                vehicle_file_path = vehicle_txt
                                break
                
                if found_usb and vehicle_file_path:
                    if last_processed_usb != str(found_usb):
                        with open(vehicle_file_path, "r", encoding="utf-8") as f:
                            vehicle_id = f.read().strip()
                            
                        if vehicle_id:
                            Clock.schedule_once(lambda dt: self.update_status(f"正在備份車號: {vehicle_id}...", (1, 1, 0, 1)))
                            success = self.do_backup(found_usb, vehicle_id)
                            
                            if success:
                                Clock.schedule_once(lambda dt: self.update_status(f"備份成功！\n車號: {vehicle_id}", (0, 1, 0, 1)))
                                last_processed_usb = str(found_usb)
                else:
                    if last_processed_usb is not None:
                        last_processed_usb = None
                        Clock.schedule_once(lambda dt: self.update_status("等待插入隨身碟...", (1, 1, 1, 1)))
                        
            except Exception as e:
                print(f"監聽發生例外: {e}")
                
            time.sleep(2)

    def do_backup(self, usb_root, vehicle_id):
        """ 執行備份複製邏輯 """
        try:
            target_base = Path("/storage/emulated/0/Documents")
            target_dir = target_base / vehicle_id
            target_dir.mkdir(parents=True, exist_ok=True)

            for item in usb_root.iterdir():
                target_item = target_dir / item.name
                if item.is_dir():
                    if target_item.exists():
                        shutil.rmtree(target_item)
                    shutil.copytree(item, target_item)
                else:
                    shutil.copy2(item, target_item)
            return True
        except Exception as e:
            print(f"複製失敗: {e}")
            return False

    def update_status(self, text, color):
        self.status_label.text = text
        self.status_label.color = color

    def on_stop(self):
        self.is_running = False

if __name__ == '__main__':
    BackupApp().run()