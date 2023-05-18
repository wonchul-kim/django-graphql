import graphene 

from blog.graphql.schemas.post import PostType
from blog.models import Post

from athena.graphql.schemas.project_name import ProjectType 
from athena.models import ProjectDB

class Query(graphene.ObjectType):
    posts = graphene.List(PostType)
    
    def resolve_posts(self, info):
        return Post.objects.all()
    
    project_all = graphene.List(ProjectType)
    def resolve_project_all(self, info):
        return ProjectDB.objects.all()
    
    project_search = graphene.List(ProjectType, project_name=graphene.String())
    def resolve_project_search(self, info, **kwargs):
        return ProjectDB.objects.filter(project_name__icontains=kwargs.get('project_name'))

