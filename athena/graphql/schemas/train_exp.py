import graphene
from graphene_django import DjangoObjectType 
from athena.models import ProjectDB, TrainExpDB 

class TrainExpType(DjangoObjectType):
    class Meta:
        model = TrainExpDB 
        fields = ('id', 'project', 'created_at', 'description')
        

class CreateTrainExp(graphene.Mutation):
    class Arguments:
        project_name = graphene.String(required=True)
        description = graphene.String(required=False)
        
    train_exp = graphene.Field(TrainExpType)
    msg = graphene.String() 
    
    @classmethod 
    def mutate(cls, self, info, project_name, description=""):
        if ProjectDB.objects.filter(project_name=project_name):
            project_db_obj = ProjectDB.objects.get(project_name=project_name)
            # project_obj = ProjectDB.objects.get(id=project_id)
            train_exp_db = TrainExpDB(project=project_db_obj)
            train_exp_db.save()

            return CreateTrainExp(train_exp=train_exp_db, msg="Successfully added!")
        else:
            return None
        
class DeleteTrainExp(graphene.Mutation):
    class Arguments:
        train_exp_id = graphene.Int(required=True)
        
    msg = graphene.String()
    
    @classmethod 
    def mutate(cls, self, info, train_exp_id):
        if TrainExpDB.objects.filter(id=train_exp_id):
            TrainExpDB.objects.get(id=train_exp_id).delete()

            return DeleteTrainExp(msg=f"train exp. id({train_exp_id}) has been deleted successfully!")
        else:
            return DeleteTrainExp(msg=f"There is no such train exp. id({train_exp_id})...")
    
       