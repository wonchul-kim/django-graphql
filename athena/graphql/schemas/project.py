from ast import Delete
import graphene
from graphene_django import DjangoObjectType 
from athena.models import ProjectDB 

class ProjectType(DjangoObjectType):
    class Meta:
        model = ProjectDB 
        fields = ('id', 'project_name', 'created_at', 'updated_at', 'description')

class CreateProject(graphene.Mutation):
    class Arguments:
        project_name = graphene.String(required=True)
        description = graphene.String(required=False)
        
    project = graphene.Field(ProjectType)
    msg = graphene.String()
    
    @classmethod 
    def mutate(cls, self, info, project_name, description=""):
        if not ProjectDB.objects.filter(project_name__icontains=project_name):
            project_db = ProjectDB(project_name=project_name, description=description)
            project_db.save()
        
            return CreateProject(project=project_db, msg=f"{project_name} has beed successfully added!")
        else:
            return CreateProject(project=None, msg=f"{project_name} already exists...")
  
        
class DeleteProject(graphene.Mutation):
    class Arguments:
        project_name = graphene.String(required=True)
        
    msg = graphene.String()
    
    @classmethod 
    def mutate(cls, self, info, project_name):
        if ProjectDB.objects.filter(project_name__icontains=project_name):
            ProjectDB.objects.get(project_name=project_name).delete()

            return DeleteProject(msg=f"Project({project_name}) has been deleted successfully!")
        else:
            return DeleteProject(msg=f"There is no such project({project_name})...")
    
       