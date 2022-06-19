import os

from uuid import uuid4
SECRET_KEY = os.getenv("SECRET_KEY",str(uuid4()))

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ.get('POSTGRES_DB', 'all'),
#         'USER': os.environ.get('POSTGRES_USER', 'all'),
#         'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'all'),
#         'HOST': os.environ.get('POSTGRES_NAME', '172.18.0.2'),
#     },
# }

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]
