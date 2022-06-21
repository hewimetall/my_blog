"""
WSGI config for project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

if not os.environ.get("DJANGO_SETTINGS_MODULE", None):
    # для случая запуска локально без докера
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.dev")

application = get_wsgi_application()
# !TODO: Разобраться почему проходять через nginx запросы на статику
application = WhiteNoise(application, root=os.environ.get("STATIC_ROOT"))
