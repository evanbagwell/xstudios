from django.contrib import admin
from django.urls import path
from api.views import return_33

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/number/', return_33),  # Endpoint to return 33
]