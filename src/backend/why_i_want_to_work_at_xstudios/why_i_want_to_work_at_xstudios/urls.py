from django.contrib import admin
from django.urls import path
from api.views import return_33

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/number/', return_33),  # Existing endpoint
    path('', return_33),  # New root endpoint
]