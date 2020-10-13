from graphene import relay
from graphene_django import DjangoObjectType

from ..models import Board
# from ..filters.board_filter import BoardFilter
from core.base_types import BaseConnection


class BoardType(DjangoObjectType):
    class Meta:
        model = Board
        filter_fields = '__all__'
        # filterset_class = BoardFilter
        interfaces = (relay.Node,)
        connection_class = BaseConnection
        fields = '__all__'
