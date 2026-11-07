[app]

# (str) Title of your application
title = 自動備份系統

# (str) Package name
package.name = usbbackup

# (str) Package domain (needed for android packaging)
package.domain = org.backup

# (list) Source files to include (let it include py)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy

# (list) Permissions
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,MANAGE_EXTERNAL_STORAGE

# (str) Supported orientations (landscape, portrait or all)
orientation = landscape

[buildozer]
log_level = 2
warn_on_root = 1