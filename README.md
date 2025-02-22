SEO Blog

SEO Blog - bu Django asosida qurilgan SEO optimallashtirilgan blog platformasi. U blog postlarini yaratish, tahrirlash va boshqarish imkoniyatlarini taqdim etadi.

Xususiyatlar

Django asosida - Kuchli va xavfsiz backend tizimi

SEO optimallashtirilgan - Meta teglari va URL tuzilmalari SEO talablariga mos

Foydalanuvchi autentifikatsiyasi - Ro'yxatdan o'tish va tizimga kirish imkoniyati

Blog postlari boshqaruvi - Post yaratish, tahrirlash va o'chirish

Kategoriya va teglar - Postlarni osongina guruhlash

Kommentariya tizimi - Foydalanuvchilar sharh qoldirishlari mumkin

O'rnatish

Loyihani lokal muhitda ishga tushirish uchun quyidagi bosqichlarni bajaring:

1. Repozitoriyani klonlash

$ git clone https://github.com/070DBEK/seo-blog.git
$ cd seo-blog

2. Virtual muhit yaratish va faollashtirish

$ python -m venv venv
$ source venv/bin/activate  # Linux/MacOS
$ venv\Scripts\activate  # Windows

3. Talab qilinadigan kutubxonalarni o'rnatish

$ pip install -r requirements.txt

4. Ma'lumotlar bazasini yaratish

$ python manage.py migrate

5. Superfoydalanuvchi yaratish (Admin panel uchun)

$ python manage.py createsuperuser

6. Serverni ishga tushirish

$ python manage.py runserver

Django server ishga tushgandan so'ng, loyihani quyidagi URL orqali ko'rishingiz mumkin:

http://127.0.0.1:8000/

Admin panelga kirish uchun:

http://127.0.0.1:8000/admin/

Foydalanish

Blog postlarini qo'shish va boshqarish uchun admin panelga kiring.

Foydalanuvchilar ro'yxatdan o'tib, sharh qoldirishlari mumkin.

Postlarni kategoriyalar va teglar orqali saralash mumkin.

Hissa qo'shish

Agar loyiha ustida ishlashni xohlasangiz, quyidagi bosqichlarni bajaring:

Repozitoriyani fork qiling.

O'zingizga tegishli o'zgarishlarni bajaring.

Pull Request yuboring.

Litsenziya

Bu loyiha MIT Litsenziyasi asosida tarqatiladi.

Muallif

070DBEK - GitHub Profil