[app]
title = Nmap Scanner
package.name = nmapapp
package.domain = org.nmapapp
source.dir = main.py
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.archs = arm64-v8a,armeabi-v7a
android.accept_sdk_license = True
p4a.branch = master
[buildozer]
log_level = 2
warn_on_root = 1
