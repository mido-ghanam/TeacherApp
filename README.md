# TeacherApp - نسخة MVP جاهزة
الواجهة بالعربية وتستخدم Bootstrap.
تشغيل محلي أو في GitHub Codespaces أو PythonAnywhere.

الخطوات لتشغيل محلياً:
1. ثبت بايثون 3.10+
2. نفذ:
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
3. افتح المتصفح على http://127.0.0.1:8000

ملاحظات للـ Codespaces:
- افتح repository في Codespaces ثم شغل نفس الأوامر داخل الـ terminal.
- رابط العرض سيظهر من Codespaces.

تعديل:
- غير SECRET_KEY في teacherproject/settings.py
- DEBUG=False قبل النشر
