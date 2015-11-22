from terrarium.conf.global_settings import *


SECRET_KEY = 'dev'

DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = True

CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False

ALLOWED_HOSTS = ('127.0.0.1', 'localhost')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'terrarium_dev',
        'HOST': 'localhost'
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
