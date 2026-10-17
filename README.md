# توزيع المدعوين - Django
## تشغيل محلي
    pip install -r requirements.txt
    python manage.py runserver
ثم افتح http://127.0.0.1:8000
- `/` المخطط وإضافة الأسماء   - `/search/` البحث   - `/view/?table=25` تظليل الطاولة
- الحفظ في `data.json` (غيّر المكان بالمتغير DATA_FILE)  - نسخة احتياطية: `/data.json`
## الاستضافة
متغيرات: DEBUG=0, SECRET_KEY, DATA_FILE (على قرص دائم), ALLOWED_HOSTS, CSRF_TRUSTED_ORIGINS=https://موقعك
أمر البناء: pip install -r requirements.txt && python manage.py collectstatic --noinput
أمر التشغيل: gunicorn config.wsgi
