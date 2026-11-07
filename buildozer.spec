[app]

# (str) Title of your application
title = USB Copy App

# (str) Package name
package.name = usbcopyapp

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (include text files, images, etc.)
source.include_exts = py,png,jpg,kv,atlas,ttc,ttf

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (list) Permissions
# 請求存取 Android 儲存空間權限
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# -----------------------------------------------------------------------------
# Android specific
# -----------------------------------------------------------------------------

# (bool) Accept SDK license agreement automatically
# 自動接受 Android SDK 授權合約（解決 CI/CD 編譯中斷的關鍵）
android.accept_sdk_license = True

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (int) Android NDK version
android.ndk = 25b

# (bool) If True, then skip buildozer touch
android.skip_update = False

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enable AndroidX support. Required when targeting API 28+
android.enable_androidx = True

# -----------------------------------------------------------------------------
# Buildozer section
# -----------------------------------------------------------------------------

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = false, 1 = true)
warn_on_root = 1
