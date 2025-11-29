[app]

# Sizin tətbiqinizin əsas adı
title = Snakeibo

# Tətbiqin adı (qısa)
package.name = snakeibo

# Tətbiqin paketi (təkrarolunmaz olmalıdır)
package.domain = com.rex.snakeibo

# Tətbiqin versiyası (nömrə)
version = 1.0.0

# Kivy proqramınızın ana faylı. ARTIQ: snakeibo_new.py
main.py = snakeibo_new.py

# Tətbiqin icon faylı (təklif olunur: icon.png)
icon.filename = %(source.dir)s/icon.png

# Requirements: Kivy-nin özü və AdMob inteqrasiyası üçün kivy-admob paketi
requirements = python3,kivy,kivy-admob==0.1.0

# Orientation: portrait, landscape, all
orientation = all

# Android-də icazə verilən minimum API səviyyəsi. (Adətən 21-dən yüksək)
android.minapi = 21

# Hədəf API səviyyəsi (Google Play üçün mütləq 33+ olmalıdır)
android.api = 33

# Java kodlarını obfuscate etmək (istəyə bağlı)
android.no_obfuscate = 1

# [build] Bölməsi: AAB yaratmaq üçün vacibdir
[build]

# SDK lisenziyasını avtomatik qəbul etmək
android.accept_sdk_license = True

# Tətbiqin ehtiyac duyduğu icazələr (Şəbəkə tələb olunur)
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# Google Mobile Ads İD-sini (APP_ID) AndroidManifest.xml-ə daxil etmək
# Bu, Kivy-AdMob üçün XÜSUSİ TƏLƏBDİR!
# Sizin APP_ID: ca-app-pub-6525217937280813~1393662594
android.extra_manifest_xml = <meta-data android:name="com.google.android.gms.ads.APPLICATION_ID" android:value="ca-app-pub-6525217937280813~1393662594"/>

# AAB faylının yaradılmasını tələb edirik (Play Store üçün)
export_orientation = False

[packaging]
# AAB faylının Play Store üçün imzalanmasını tələb edir
android.release = True
