"""
WSGI config for zhougongjin52 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zhougongjin52.settings')

application = get_wsgi_application()
sys.path.append("/root/myDjango/myDjango_env/zhougongjin52/")

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
