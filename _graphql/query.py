from ast import Sub
import graphene 

from athena.models import ProjectDB, SubProjectDB, TrainExpDB, TrainEpochTrainLogDB, TrainEpochValLogDB
from athena.graphql.schemas.project import ProjectType
from athena.graphql.schemas.sub_project import SubProjectType
from athena.graphql.schemas.train_exp import TrainExpType
from athena.graphql.schemas.train_epoch_train_log import TrainEpochTrainLogType
from athena.graphql.schemas.train_epoch_val_log import TrainEpochValLogType

class Query(graphene.ObjectType):
    ### for ProjectDB #############################################
    project_all = graphene.List(ProjectType)
    def resolve_project_all(self, info):
        return ProjectDB.objects.all()
    
    project_search = graphene.Field(ProjectType, project_name=graphene.String())
    def resolve_project_search(self, info, project_name):
        if ProjectDB.objects.filter(project_name=project_name):
            return ProjectDB.objects.get(project_name=project_name)

    ### for SubProjectDB #############################################
    sub_project_all = graphene.List(SubProjectType)
    def resolve_sub_project_all(self, info):
        return SubProjectDB.objects.all()
    
    sub_project_by_project_name = graphene.Field(SubProjectType, project_name=graphene.String())
    def resolve_sub_project_by_project_name(self, info, project_name):
        if ProjectDB.objects.filter(project_name=project_name):
            project_db_obj = ProjectDB.objects.get(project_name=project_name)
            
            if SubProjectDB.objects.filter(project=project_db_obj):
                return SubProjectDB.objects.get(project=project_db_obj)
            else:
                print(f"There is no such project({project_name}) in sub-project db")
                return None 
        else:
            print(f"There is no such project({project_name}) in project db")
            return None

    ### for TrainExpDB #############################################
    train_exp_all = graphene.List(TrainExpType)
    def resolve_train_exp_all(self, info):
        return TrainExpDB.objects.all()
    
    train_exp_by_project = graphene.List(TrainExpType, project_name=graphene.String())
    def resolve_train_exp_by_project(self, info, project_name):
        if ProjectDB.objects.filter(project_name=project_name):
            project_db_obj = ProjectDB.objects.get(project_name=project_name)
            return TrainExpDB.objects.get(project=project_db_obj)
    
    train_exp_by_id = graphene.Field(TrainExpType, train_exp_id=graphene.Int())
    def resolve_train_exp_by_id(self, info, train_exp_id):
        if TrainExpDB.objects.filter(id=train_exp_id):
            return TrainExpDB.objects.get(id=train_exp_id)
        
    ### for TrainEpochTrainLogDB #############################################
    train_epoch_train_log_all = graphene.List(TrainEpochTrainLogType)
    def resolve_train_epoch_train_log_all(self, info):
        return TrainEpochTrainLogDB.objects.all()
    
    train_epoch_train_log_all_by_train_exp = graphene.List(TrainEpochTrainLogType, train_exp=graphene.Int())
    def resolve_train_epoch_train_log_all_by_train_exp(self, info, train_exp):
        if TrainExpDB.objects.filter(id=train_exp):
            train_exp_ojb = TrainExpDB.objects.get(id=train_exp)
            if TrainEpochTrainLogDB.objects.filter(train_exp=train_exp_ojb):
                return TrainEpochTrainLogDB.objects.filter(train_exp=train_exp_ojb)
    
    ### for TrainEpochValLogDB #############################################
    train_epoch_val_log_all = graphene.List(TrainEpochValLogType)
    def resolve_train_epoch_val_log_all(self, info):
        return TrainEpochValLogDB.objects.all()
    
    train_epoch_val_log_all_by_train_exp = graphene.List(TrainEpochValLogType, train_exp=graphene.Int())
    def resolve_train_epoch_val_log_all_by_train_exp(self, info, train_exp):
        if TrainExpDB.objects.filter(id=train_exp):
            train_exp_ojb = TrainExpDB.objects.get(id=train_exp)
            if TrainEpochValLogDB.objects.filter(train_exp=train_exp_ojb):
                return TrainEpochValLogDB.objects.filter(train_exp=train_exp_ojb)