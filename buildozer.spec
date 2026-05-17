[app]

title = Billing App
package.name = billingapp
package.domain = org.billing

source.dir = .
source.include_exts = py,png,jpg,kv

version = 1.0

requirements = python3,kivy,reportlab

orientation = portrait

fullscreen = 0

android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

[buildozer]

log_level = 2
warn_on_root = 1
