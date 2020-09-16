from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Board
from .serializers import BoardSerializer


class BoardViewSet(ModelViewSet):
    model = Board
    serializer_class = BoardSerializer

    def get_queryset(self):
        return Board.objects.all()
