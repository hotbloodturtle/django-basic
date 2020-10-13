import graphene
from graphene_django.filter import DjangoFilterConnectionField

from .models import Board
from .types.board_types import BoardType


class BoardsQueries(graphene.ObjectType):
    boards = DjangoFilterConnectionField(BoardType)
