# django-basic-network

## Installation

The BasicNetwork project needs [Python3](url_python) to run.

Follow the next steps in order to install it:

Create a new directory and enter in it:

```sh
mkdir BasicNetworkProject
cd BasicNetworkProject
```

Create a virtual environment for the project:

```sh
python3 -m venv env
source env/bin/activate
```

Now you should see an indicator on the left side of your terminal command line, something like this on Mac:

```sh
(env) MacBook-Pro-de-Raul:django-basic-network raul$ 
```
Next, install Django dependencies on the recently activated environment:

```sh
pip install django
```

Now we have Django command line installed, so we could start our local project and configure it propperly. NOTICE the dot at the end of the command.

```sh
django-admin startproject BasicNetwork .
```

Your system is capable enough to run the current project as it is already, however we want to make sure the Posts and Profiles applications are bounded to the BasicNetwork, and we have updated it basic configuration before start it up.

UPDATE BasicNetwork/settings.py:
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
       +'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

ADD TO BasicNetwork/settings.py:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
   +
   +'posts',
   +'profiles',
]
```

APPEND TO BasicNetwork/settings.py:
```python
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
```

This way you can utterly confident run your server by executing this following commands. Take into account that you will need to repeat some of them in the future, so you will understand them better later on. For now, just believe me:

```sh
python manage.py migrate
python manage.py createsuperuser    # You will be prompt for username,
                                    # email, and password. Fill it.
python manage.py runserver
```

