from .base import *

DEBUG = False

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
        'level': 'DEBUG',
    },
}

try:
    from .local import *
except ImportError:
    pass
