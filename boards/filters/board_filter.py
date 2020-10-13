from django_filters import rest_framework as filters

from ..models import Board


class BoardFilter(filters.FilterSet):
    class Meta:
        model = Board
        fields = []
