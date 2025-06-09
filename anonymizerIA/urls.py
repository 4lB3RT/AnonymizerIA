from django.contrib import admin
from django.urls import include, path

from anonymizerIA.src.Infrastructure.Controllers import GenerateDatabaseDataController

urlpatterns = [
    path('database/generate/', GenerateDatabaseDataController.GenerateDatabaseDataController.as_view()),
    path('admin/', admin.site.urls),
]