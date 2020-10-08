import graphene

from boards.schema import Query as BoardsQuery


class Query(BoardsQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)