import os

from terrarium.conf.global_settings import *


VHOST_DIR = os.environ.get('VHOST_DIR', ROOT_DIR)

ALLOWED_HOSTS = [os.environ.get('HOSTNAME', 'localhost')]

SECRET_KEY = os.environ.get('SECRET_KEY', '*' * 10)

CSRF_COOKIE_SECURE = SESSION_COOKIE_SECURE = bool(int(os.environ.get('COOKIE_SECURE', '1')))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_NAME', PROJECT_NAME),
        'USER': os.environ.get('DB_USER', PROJECT_NAME),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
    }
}

STATIC_ROOT = os.path.normpath(os.path.join(VHOST_DIR, 'web', 'static'))
MEDIA_ROOT = os.path.normpath(os.path.join(VHOST_DIR, 'web', 'media'))
MEDIA_URL = '/media/'

DEFAULT_FROM_EMAIL = SERVER_EMAIL = os.environ.get('EMAIL_SENDER', '{0}@{1}'.format(
    PROJECT_NAME, os.environ.get('HOSTNAME', 'localhost')))

ADMINS = [('admin', DEFAULT_FROM_EMAIL)]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.normpath(os.path.join(VHOST_DIR, 'log', 'django.log')),
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        }
    },
    'formatters': {
        'verbose': {
            'format':
                '[%(asctime)s] %(levelname)s:%(name)s %(funcName)s %(message)s',
        },
    },
    'loggers': {
        '': {
            'level': 'WARNING',
            'handlers': ['file', 'mail_admins'],
        },
    }
}
