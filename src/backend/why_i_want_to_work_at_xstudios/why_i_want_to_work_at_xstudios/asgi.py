"""
ASGI config for why_i_want_to_work_at_xstudios project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'why_i_want_to_work_at_xstudios.settings')

application = get_asgi_application()
