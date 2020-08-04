from django.contrib import admin
from django.urls import path
from .views import alive_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alive', alive_view),
]
