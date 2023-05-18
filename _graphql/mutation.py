from calendar import c
import graphene 

from athena.graphql.schemas.project import CreateProject, DeleteProject
from athena.graphql.schemas.train_exp import CreateTrainExp, DeleteTrainExp
from athena.graphql.schemas.train_epoch_log import CreateTrainEpochLog
class Mutation(graphene.ObjectType):
    ### for ProjectDB
    create_project = CreateProject.Field()
    delete_project = DeleteProject.Field()
    
    ### for TrainExpDB
    create_train_exp = CreateTrainExp.Field() 
    delete_train_exp = DeleteTrainExp.Field()
    
    ### for TrainEpochLogDB
    create_train_epoch_log = CreateTrainEpochLog.Field()
    
    ### for TrainStepLogDB