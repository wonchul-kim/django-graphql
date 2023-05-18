from athena.graphql.schemas.train_epoch_log import TrainEpochLogType
import graphene 

from athena.graphql.schemas.project_name import ProjectType
from athena.graphql.schemas.train_exp import TrainExpType
from athena.models import ProjectDB, TrainExpDB, TrainEpochLogDB

class Query(graphene.ObjectType):
    ### for ProjectDB #############################################
    project_all = graphene.List(ProjectType)
    def resolve_project_all(self, info):
        return ProjectDB.objects.all()
    
    project_search = graphene.Field(ProjectType, project_name=graphene.String())
    def resolve_project_search(self, info, project_name):
        if ProjectDB.objects.filter(project_name__icontains=project_name):
            return ProjectDB.objects.get(project_name=project_name)

    ### for TrainExpDB #############################################
    train_exp_all = graphene.List(TrainExpType)
    def resolve_train_exp_all(self, info):
        return TrainExpDB.objects.all()
    
    train_exp_by_project = graphene.List(TrainExpType, project_name=graphene.String())
    def resolve_train_exp_by_project(self, info, project_name):
        if ProjectDB.objects.filter(project_name=project_name):
            project_db_obj = ProjectDB.objects.get(project_name=project_name)
            return TrainExpDB.objects.filter(project=project_db_obj)
    
    ## FIXME: not working......!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    train_exp_by_id = graphene.Field(TrainExpType, train_exp_id=graphene.Int())
    def resolve_train_exp_by_id(self, info, train_exp_id):
        if TrainExpDB.objects.filter(id=train_exp_id):
            return TrainExpDB.objects.get(id=train_exp_id)
        
    ### for TrainEpochLogDB #############################################
    train_epoch_log_all = graphene.List(TrainEpochLogType)
    def resolve_train_epoch_log_all(self, info):
        return TrainEpochLogDB.objects.all()
    
    train_epoch_log_all_by_train_exp = graphene.List(TrainEpochLogType, train_exp=graphene.Int())
    def resolve_train_epoch_log_all_by_train_exp(self, info, train_exp):
        if TrainExpDB.objects.filter(id=train_exp):
            train_exp_ojb = TrainExpDB.objects.get(id=train_exp)
            if TrainEpochLogDB.objects.filter(train_exp=train_exp_ojb):
                return TrainEpochLogDB.objects.filter(train_exp=train_exp_ojb)
    
