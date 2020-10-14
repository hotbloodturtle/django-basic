import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField

from .models import Board
from .types.board_types import BoardType


class BoardsQueries(graphene.ObjectType):
    board = relay.Node.Field(BoardType)
    boards = DjangoFilterConnectionField(BoardType)
