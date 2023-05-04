import graphene 

from .schemas.post import PostType
from ..models import Post

class Query(graphene.ObjectType):
    posts = graphene.List(PostType)
    
    def resolve_posts(self, info):
        return Post.objects.all()

