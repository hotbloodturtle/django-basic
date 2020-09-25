from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import alive_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alive', alive_view),
    path('boards/', include('boards.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)