import graphene
from graphene_django import DjangoObjectType 
from athena.models import TrainExpDB, TrainEpochLogDB

class TrainEpochLogType(DjangoObjectType):
    class Meta:
        model = TrainEpochLogDB 
        fields = ('id', 'train_exp', 'epoch', 'log', 'created_at')
        

class CreateTrainEpochLog(graphene.Mutation):
    class Arguments:
        train_exp = graphene.Int(required=True)
        epoch = graphene.Int(required=True)
        log = graphene.types.json.JSONString(required=True)
        
    train_epoch_log = graphene.Field(TrainEpochLogType)
    msg = graphene.String() 
    
    @classmethod 
    def mutate(cls, self, info, train_exp, epoch, log):
        if TrainExpDB.objects.filter(id=train_exp):
            train_exp_db_obj = TrainExpDB.objects.get(id=train_exp)
            train_epoch_log_db = TrainEpochLogDB(train_exp=train_exp_db_obj, epoch=epoch, log=log)
            train_epoch_log_db.save()

            return CreateTrainEpochLog(train_epoch_log=train_epoch_log_db, msg="Successfully added!")
        else:
            return CreateTrainEpochLog(train_epoch_log=None, msg=f"There is no such train exp. id({train_exp}) added!")
        

       