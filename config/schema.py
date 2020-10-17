import graphene

from boards.schema import BoardsQueries, BoardsMutations


class Query(BoardsQueries):
    pass


class Mutation(BoardsMutations):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
