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

try:
    from .local import *
except ImportError:
    pass
