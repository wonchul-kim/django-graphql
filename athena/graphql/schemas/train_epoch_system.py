import graphene
from graphene_django import DjangoObjectType 
from athena.models import TrainExpDB, TrainEpochSystemDB

class TrainEpochSystemType(DjangoObjectType):
    class Meta:
        model = TrainEpochSystemDB 
        fields = ('id', 'train_exp', 'epoch', 'system', 'created_at')
        

class CreateTrainEpochSystem(graphene.Mutation):
    class Arguments:
        train_exp = graphene.Int(required=True)
        epoch = graphene.Int(required=True)
        system = graphene.types.json.JSONString(required=True)
        
    train_epoch_system = graphene.Field(TrainEpochSystemType)
    msg = graphene.String() 
    
    @classmethod 
    def mutate(cls, self, info, train_exp, epoch, system):
        if TrainExpDB.objects.filter(id=train_exp):
            train_exp_db_obj = TrainExpDB.objects.get(id=train_exp)
            train_epoch_system_db = TrainEpochSystemDB(train_exp=train_exp_db_obj, epoch=epoch, system=system)
            train_epoch_system_db.save()

            return CreateTrainEpochSystem(train_epoch_system=train_epoch_system_db, msg="Successfully added!")
        else:
            return CreateTrainEpochSystem(train_epoch_system=None, msg=f"There is no such train exp. id({train_exp}) added!")       
        