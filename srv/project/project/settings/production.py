from .base import *
from uuid import uuid4
SECRET_KEY = os.getenv("SECRET_KEY", str(uuid4()))

DEBUG = False

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', 'pgdb'),
        'USER': os.environ.get('POSTGRES_USER', 'irk'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'irk'),
        'HOST': os.environ.get('POSTGRES_NAME', 'localhost'),
    },
}

# settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
}