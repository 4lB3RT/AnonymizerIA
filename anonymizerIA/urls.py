<<<<<<< HEAD
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('images/', include('images.urls')),
    path('admin/', admin.site.urls),
=======
from django.urls import path, include
from anonymizerIA.src.Infrastructure.Controllers.CreateImageController import CreateImageController

urlpatterns = [
    path('images/create', CreateImageController.as_view(), name="create"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
>>>>>>> a2326fa (initial commit)
]