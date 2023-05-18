import graphene 

from blog.graphql.schemas.post import PostMutation

from athena.graphql.schemas.project_name import CreateProject

class Mutation(graphene.ObjectType):
    create_post = PostMutation.Field()  
    create_project = CreateProject.Field()