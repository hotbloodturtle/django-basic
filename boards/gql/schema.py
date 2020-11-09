import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField

from ..models import Board
from .mutations.board_mutations import CreateBoardMutation, UpdateBoardMutation
from .types.board_types import BoardType


class BoardsQueries(graphene.ObjectType):
    board = relay.Node.Field(BoardType)
    boards = DjangoFilterConnectionField(BoardType)


class BoardsMutations(graphene.ObjectType):
    create_board = CreateBoardMutation.Field()
    update_board = UpdateBoardMutation.Field()
    