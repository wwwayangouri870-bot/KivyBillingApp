[app]

title = KivyBillingApp

package.name = kivybillingapp
package.domain = org.kivy

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3==3.10.11,kivy==2.3.0

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

android.accept_sdk_license = True
android.api = 33
android.minapi = 21
android.ndk = 25b

p4a.branch = master

log_level = 2
warn_on_root = 1
