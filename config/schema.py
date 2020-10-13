import graphene

from boards.schema import BoardsQueries


class Query(BoardsQueries):
    pass


schema = graphene.Schema(query=Query)