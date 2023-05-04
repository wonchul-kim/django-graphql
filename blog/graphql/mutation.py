import graphene 

from .schemas.post import PostMutation

class Mutation(graphene.ObjectType):
    create_post = PostMutation.Field()  