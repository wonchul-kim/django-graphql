from calendar import c
import graphene 

from athena.graphql.schemas.health_check import CreateHealthCheck

from athena.graphql.schemas.project import CreateProject, DeleteProject
from athena.graphql.schemas.sub_project import CreateSubProject, DeleteSubProject
from athena.graphql.schemas.train_exp import CreateTrainExp, DeleteTrainExp
from athena.graphql.schemas.train_exp_server_info import CreateTrainExpServerInfo
from athena.graphql.schemas.train_exp_train_info import CreateTrainExpTrainInfo
from athena.graphql.schemas.train_epoch_train_log import CreateTrainEpochTrainLog
from athena.graphql.schemas.train_epoch_system import CreateTrainEpochSystem
from athena.graphql.schemas.train_epoch_val_log import CreateTrainEpochValLog

class Mutation(graphene.ObjectType):
    ### for health-check
    create_health_check = CreateHealthCheck.Field()
    
    ### for ProjectDB
    create_project = CreateProject.Field()
    delete_project = DeleteProject.Field()
    
    ### for Sub-ProjectDB
    create_sub_project = CreateSubProject.Field()
    delete_sub_project = DeleteSubProject.Field()
    
    ### for TrainExpDB
    create_train_exp = CreateTrainExp.Field() 
    delete_train_exp = DeleteTrainExp.Field()
    
    ### for trainExpServerInfoDB
    create_train_exp_server_info = CreateTrainExpServerInfo.Field()

    ### for trainExpTrainInfoDB
    create_train_exp_train_info = CreateTrainExpTrainInfo.Field()
    
    
    ### for TrainEpochTrainLogDB
    create_train_epoch_train_log = CreateTrainEpochTrainLog.Field()
    
    ### for TrainEpochSystem
    create_train_epoch_system  = CreateTrainEpochSystem.Field()
    
    ### for TrainEpochValLogDB
    create_train_epoch_val_log = CreateTrainEpochValLog.Field()
    