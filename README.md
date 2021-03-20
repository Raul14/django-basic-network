# django-basic-network
python3 -m venv env
source env/bin/activate
->(env) MacBook-Pro-de-Raul:django-basic-network raul$
pip install django
->pip freeze:
    (env) MacBook-Pro-de-Raul:django-basic-network raul$ pip freeze
    asgiref==3.3.1
    Django==3.1.7
    pytz==2021.1
    sqlparse==0.4.1
django-admin startproject BasicNetwork .
->ls:
    (env) MacBook-Pro-de-Raul:django-basic-network raul$ ls
    BasicNetwork    README.md       env             manage.py
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
->browser
UPDATE BasicNetwork/settings.py:
    -'DIRS': [],
    +'DIRS': [BASE_DIR / 'templates'],
ADD TO BasicNetwork/settings.py:L40:
    +    'posts',
    +    'profiles',
ADD TO BasicNetwork/settings.py:L40:
    +STATIC_ROOT = BASE_DIR / 'static'
    +
    +STATIC_POSTS = STATIC_ROOT / 'posts'
    +STATIC_PROFILES = STATIC_ROOT / 'profiles'
    +
    +STATICFILES_DIRS = [
    +    STATIC_ROOT,
    +    STATIC_POSTS,
    +    STATIC_PROFILES,
    +]
    +
    +MEDIA_URL = '/media/'
    +MEDIA_ROOT = BASE_DIR / 'media'
/IGNORE:
    python manage.py startapp posts
    