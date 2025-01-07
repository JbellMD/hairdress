"""
WSGI config for hairdresser_django project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hairdresser_django.settings')

application = get_wsgi_application()
