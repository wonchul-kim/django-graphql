import graphene
from graphene_django import DjangoObjectType 
from athena.models import TrainExpDB, TrainEpochValLogDB

class TrainEpochValLogType(DjangoObjectType):
    class Meta:
        model = TrainEpochValLogDB 
        fields = ('id', 'train_exp', 'epoch', 'log', 'created_at')
        

class CreateTrainEpochValLog(graphene.Mutation):
    class Arguments:
        train_exp = graphene.Int(required=True)
        epoch = graphene.Int(required=True)
        log = graphene.types.json.JSONString(required=True)
        
    train_epoch_val_log = graphene.Field(TrainEpochValLogType)
    msg = graphene.String() 
    
    @classmethod 
    def mutate(cls, self, info, train_exp, epoch, log):
        if TrainExpDB.objects.filter(id=train_exp):
            train_exp_db_obj = TrainExpDB.objects.get(id=train_exp)
            train_epoch_val_log_db = TrainEpochValLogDB(train_exp=train_exp_db_obj, epoch=epoch, log=log)
            train_epoch_val_log_db.save()

            return CreateTrainEpochValLog(train_epoch_val_log=train_epoch_val_log_db, msg="Successfully added!")
        else:
            return CreateTrainEpochValLog(train_epoch_val_log=None, msg=f"There is no such train exp. id({train_exp}) added!")
        

       