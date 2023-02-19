from django.urls import path

from images.Infrastructure.GetImageController import GetImageController
from images.Infrastructure.CreateImageController import CreateImageController

urlpatterns = [
    path('', GetImageController, name='index'),
    path('create', CreateImageController, name='index'),
]