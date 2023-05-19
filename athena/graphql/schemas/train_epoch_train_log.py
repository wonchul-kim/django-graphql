from urllib import request
import graphene
from graphene_django import DjangoObjectType 
from athena.models import TrainExpDB, TrainEpochTrainLogDB

class TrainEpochTrainLogType(DjangoObjectType):
    class Meta:
        model = TrainEpochTrainLogDB 
        fields = ('id', 'train_exp', 'epoch', 'log', 'created_at')
        

class CreateTrainEpochTrainLog(graphene.Mutation):
    class Arguments:
        train_exp = graphene.Int(required=True)
        epoch = graphene.Int(required=True)
        log = graphene.types.json.JSONString(required=True)
        
    train_epoch_train_log = graphene.Field(TrainEpochTrainLogType)
    msg = graphene.String() 
    
    @classmethod 
    def mutate(cls, self, info, train_exp, epoch, log):
        if TrainExpDB.objects.filter(id=train_exp):
            train_exp_db_obj = TrainExpDB.objects.get(id=train_exp)
            train_epoch_train_log_db = TrainEpochTrainLogDB(train_exp=train_exp_db_obj, epoch=epoch, log=log)
            train_epoch_train_log_db.save()

            return CreateTrainEpochTrainLog(train_epoch_train_log=train_epoch_train_log_db, msg="Successfully added!")
        else:
            return CreateTrainEpochTrainLog(train_epoch_train_log=None, msg=f"There is no such train exp. id({train_exp}) added!")
        

       