import graphene 

from blog.graphql.schemas.post import PostType
from blog.models import Post

from athena.graphql.schemas.project_name import ProjectType 
from athena.models import ProjectDB

class Query(graphene.ObjectType):
    posts = graphene.List(PostType)
    
    def resolve_posts(self, info):
        return Post.objects.all()
    
    all_projects = graphene.List(ProjectType)
    def resolve_all_projects(self, info):
        return ProjectDB.objects.all()

