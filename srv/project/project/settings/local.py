import os

from uuid import uuid4
SECRET_KEY = os.getenv("SECRET_KEY",str(uuid4()))
docker- = os.getenv("SECRET_KEY",str(uuid4()))

    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', 'pgdb'),
        'USER': os.environ.get('POSTGRES_USER', 'irk'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'irk'),
        'HOST': os.environ.get('POSTGRES_NAME', 'localhost'),
    },

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]
