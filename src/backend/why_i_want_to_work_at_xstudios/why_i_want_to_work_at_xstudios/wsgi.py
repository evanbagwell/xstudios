# /var/www/xstudios/src/backend/why_i_want_to_work_at_xstudios/wsgi.py

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'why_i_want_to_work_at_xstudios.settings')

application = get_wsgi_application()
