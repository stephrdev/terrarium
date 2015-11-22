import logging
import os

from terrarium.conf.global_settings import *


RESOURCES_DIR = os.path.join(os.path.dirname(__file__), 'resources')

SECRET_KEY = 'testsecret01234567890'

DEBUG = TEMPLATE_DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

# Disable logging for unittests.
logging.disable(logging.CRITICAL)
