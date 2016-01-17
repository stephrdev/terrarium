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
TIME_ZONE = 'Europe/Berlin'
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = os.path.join(ROOT_DIR, 'web', 'media')
MEDIA_URL = '/media/'

STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'
STATICFILES_DIRS = [os.path.join(ROOT_DIR, 'static')]
STATIC_ROOT = os.path.join(ROOT_DIR, 'web', 'static')
STATIC_URL = '/static/'

PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.jsmin.JSMinCompressor'
PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.NoopCompressor'

PIPELINE_CSS = {
    'styles': {
        'source_filenames': (
            'css/styles.css',
            'css/vendor/metricsgraphics/metricsgraphics-2.7.0.css',
        ),
        'output_filename': 'css/build.css',
    },
}

PIPELINE_JS = {
    'scripts': {
        'source_filenames': (
            'js/vendor/jquery/jquery-2.1.4.js',
            'js/vendor/d3/d3-3.5.10.js',
            'js/vendor/metricsgraphics/metricsgraphics-2.7.0.js',
            'js/graph.js',
            'js/app.js',
        ),
        'output_filename': 'js/build.js',
    }
}

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
                'django.template.context_processors.tz',
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

    'pipeline',
    'rest_framework',
    'rest_framework.authtoken',
    'didadata',
    'howl',

    'terrarium.api',
    'terrarium.watchdog',
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
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'drf_ujson.renderers.UJSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'drf_ujson.parsers.UJSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 250,
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

PUSHOVER_TOKEN = ''
PUSHOVER_RECIPIENT = ''
