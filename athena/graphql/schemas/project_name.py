from importlib.metadata import requires
from pydoc import describe
from typing_extensions import Required
import graphene
from graphene_django import DjangoObjectType 
from athena.models import ProjectDB 

from django.template.defaultfilters import slugify

class ProjectType(DjangoObjectType):
    class Meta:
        model = ProjectDB 
        fields = ('id', 'project_name', 'created_at', 'updated_at', 'description')
        

class CreateProject(graphene.Mutation):
    class Arguments:
        project_name = graphene.String(required=True)
        description = graphene.String(required=False)
        
    project = graphene.Field(ProjectType)
    
    @classmethod 
    def mutate(cls, self, info, **kwargs):
        project_name = kwargs['project_name']
        if 'description' in kwargs.keys():
            description = kwargs['description']
        else:
            description = ""
            
        project_db = ProjectDB(project_name=project_name, description=description)
        project_db.save()
        
        return CreateProject(project=project_db)