from django.urls import path

from .views import BoardViewSet

urlpatterns = [
    path('', BoardViewSet.as_view(
        {'get': 'list', 'post': 'create'}), name='boards'),
    path('<int:pk>/',
         BoardViewSet.as_view({'get': 'retrieve', 'patch': 'update', 'delete': 'destroy'}), name='boards'),
]
