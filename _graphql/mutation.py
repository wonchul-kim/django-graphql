from calendar import c
import graphene 

from athena.graphql.schemas.project import CreateProject, DeleteProject
from athena.graphql.schemas.train_exp import CreateTrainExp, DeleteTrainExp
from athena.graphql.schemas.train_exp_server_info import CreateTrainExpServerInfo
from athena.graphql.schemas.train_exp_train_info import CreateTrainExpTrainInfo
from athena.graphql.schemas.train_epoch_train_log import CreateTrainEpochTrainLog
from athena.graphql.schemas.train_epoch_val_log import CreateTrainEpochValLog

class Mutation(graphene.ObjectType):
    ### for ProjectDB
    create_project = CreateProject.Field()
    delete_project = DeleteProject.Field()
    
    ### for TrainExpDB
    create_train_exp = CreateTrainExp.Field() 
    delete_train_exp = DeleteTrainExp.Field()
    
    ### for trainExpServerInfoDB
    create_train_exp_server_info = CreateTrainExpServerInfo.Field()
    create_train_exp_train_info = CreateTrainExpTrainInfo.Field()

    ### for trainExpTrainInfoDB
    
    ### for TrainEpochTrainLogDB
    create_train_epoch_train_log = CreateTrainEpochTrainLog.Field()
    
    ### for TrainEpochValLogDB
    create_train_epoch_val_log = CreateTrainEpochValLog.Field()
    