from django.urls import path

from .views import BoardViewSet

app_name = 'boards'

urlpatterns = [
    path('', BoardViewSet.as_view(
        {'get': 'list', 'post': 'create'}), name='list'),
    path('<int:pk>/',
         BoardViewSet.as_view({'get': 'retrieve', 'patch': 'update', 'delete': 'destroy'}), name='detail'),
]
