import os


PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_NAME = os.path.basename(PROJECT_DIR)
ROOT_DIR = os.path.dirname(PROJECT_DIR)

SECRET_KEY = 'terrarium'

DEBUG = False

DEFAULT_FROM_EMAIL = 'root@localhost'
SERVER_EMAIL = 'root@localhost'
EMAIL_SUBJECT_PREFIX = '[{0}] '.format(PROJECT_NAME)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'terrarium',
    }
}

ALLOWED_HOSTS = []
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SITE_ID = 1

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = os.path.join(ROOT_DIR, 'web', 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(ROOT_DIR, 'web', 'static')
STATIC_URL = '/static/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(ROOT_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': False,
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

ROOT_URLCONF = 'terrarium.urls'

WSGI_APPLICATION = 'terrarium.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
    'didadata',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    )
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}
