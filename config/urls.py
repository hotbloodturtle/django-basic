from django.contrib import admin
from django.urls import path, include
from .views import alive_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alive', alive_view),
    path('boards/', include('boards.urls')),
]
