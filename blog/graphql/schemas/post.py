import graphene
from graphene_django import DjangoObjectType
from blog.models import Post 

from django.template.defaultfilters import slugify

class PostType(DjangoObjectType):
    class Meta:
        model = Post 
        fields = ('id', 'title', 'content')
        
class PostMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        content = graphene.String(required=True)
        
    post = graphene.Field(PostType)
    
    @classmethod 
    def mutate(cls, self, info, title, content):
        post = Post(title=title, content=content, slug=slugify(title))
        post.save()
        
        return PostMutation(post=post)
    