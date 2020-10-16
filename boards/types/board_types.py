import graphene
from graphene import relay
from graphene_django import DjangoObjectType

from ..models import Board
from ..filters.board_filter import BoardFilter
from core.base_types import BaseConnection


class BoardType(DjangoObjectType):
    class Meta:
        model = Board
        filterset_class = BoardFilter
        interfaces = (relay.Node,)
        connection_class = BaseConnection
        fields = '__all__'
    
    photo = graphene.String()
    def resolve_photo(self, info):    
        if self.photo:
            return self.photo.url
        return 'no image'
    
    custom_field = graphene.String()
    def resolve_custom_field(self, info):
        return "I'm custom field"
