from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('images/', include('images.urls')),
    path('admin/', admin.site.urls),
]