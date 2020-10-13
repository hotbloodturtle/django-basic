import graphene
from graphene_django.types import DjangoObjectType

from boards.models import Board


class BoardType(DjangoObjectType):
    class Meta:
        model = Board


class BoardsQueries(graphene.ObjectType):
    board = graphene.Field(BoardType, id=graphene.Int(), title=graphene.String(), content=graphene.String())
    all_boards = graphene.List(BoardType)

    def resolve_all_boards(self, info, **kwargs):
        return Board.objects.all()

    def resolve_board(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Board.objects.get(pk=id)
