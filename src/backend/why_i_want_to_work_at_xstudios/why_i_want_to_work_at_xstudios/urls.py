from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
import os
from api.views import return_33

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/number/', return_33),  # Existing endpoint
    path('', return_33),  # New root endpoint
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'why_i_want_to_work_at_xstudios', 'static'))
