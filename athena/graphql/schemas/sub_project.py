import graphene
from graphene_django import DjangoObjectType 
from athena.models import ProjectDB, SubProjectDB

class SubProjectType(DjangoObjectType):
    class Meta:
        model = SubProjectDB 
        fields = ('id', 'project_name', 'sub_project_name', 'created_at', 'updated_at', 'description')

class CreateSubProject(graphene.Mutation):
    class Arguments:
        project_name = graphene.String(required=True)
        sub_project_name = graphene.String(required=True)
        description = graphene.String(required=False)
        
    sub_project = graphene.Field(SubProjectType)
    msg = graphene.String()
    
    @classmethod 
    def mutate(cls, self, info, project_name, sub_project_name, description=""):
        if ProjectDB.objects.filter(project_name=project_name):
            project_db_obj = ProjectDB.objects.get(project_name=project_name)
            if not SubProjectDB.objects.filter(project=project_db_obj, sub_project_name=sub_project_name):
                sub_project_db = SubProjectDB(project=project_db_obj, sub_project_name=sub_project_name, description=description)
                sub_project_db.save()
        
                return CreateSubProject(sub_project=sub_project_db, msg=f"Sub-project({sub_project_name}) has beed successfully added project({project_name})!")
            else:
                CreateSubProject(sub_project=None, msg=f"Sub-project({sub_project_name}) already exists...")
        else:
            return CreateSubProject(sub_project=None, msg=f"There is no such project({project_name})...")
  
        
class DeleteSubProject(graphene.Mutation):
    class Arguments:
        sub_project_name = graphene.String(required=True)
        
    msg = graphene.String()
    
    @classmethod 
    def mutate(cls, self, info, sub_project_name):
        if SubProjectDB.objects.filter(sub_project_name=sub_project_name):
            SubProjectDB.objects.get(sub_project_name=sub_project_name).delete()

            return DeleteSubProject(msg=f"Sub-Project({sub_project_name}) has been deleted successfully!")
        else:
            return DeleteSubProject(msg=f"There is no such sub-project({sub_project_name})...")
    
       