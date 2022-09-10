"""
WSGI config for QR_Code_based_citizen_feedback_system_for_Gujarat_Police project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'QR_Code_based_citizen_feedback_system_for_Gujarat_Police.settings')

application = get_wsgi_application()
