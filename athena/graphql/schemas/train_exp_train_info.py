import graphene
from graphene_django import DjangoObjectType 
from athena.models import TrainExpDB, TrainExpTrainInfoDB

class TrainExpTrainInfoType(DjangoObjectType):
    class Meta:
        model = TrainExpTrainInfoDB 
        fields = ('id', 'train_exp', 'parameters', 'configurations', 'options', 'description', \
                    'task', 'model_name', 'last_epoch', 'resume')

class CreateTrainExpTrainInfo(graphene.Mutation):
    class Arguments:
        train_exp = graphene.Int(required=True)
        
        parameters = graphene.types.json.JSONString(required=False)
        configurations = graphene.types.json.JSONString(required=False)
        options = graphene.types.json.JSONString(required=False)
        description = graphene.String(required=False)

        task = graphene.String(required=False)
        model_name = graphene.String(required=False)
        last_epoch = graphene.Int(required=False)
        resume = graphene.Boolean(required=False)
        
    train_exp_train_info = graphene.Field(TrainExpTrainInfoType)
    msg = graphene.String() 
    
    @classmethod 
    def mutate(cls, self, info, train_exp, parameters={}, configurations={}, options={}, description="", \
                    task="", model_name="", last_epoch=-1, resume=False):
        if TrainExpDB.objects.filter(id=train_exp):
            train_exp_db_obj = TrainExpDB.objects.get(id=train_exp)
            train_exp_train_info_db = TrainExpTrainInfoDB(train_exp=train_exp_db_obj, \
                                        parameters=parameters, configurations=configurations, options=options, description=description, \
                                        task=task, model_name=model_name, last_epoch=last_epoch, resume=resume)
            train_exp_train_info_db.save()

            return CreateTrainExpTrainInfo(train_exp_train_info=train_exp_train_info_db, msg="Successfully added!")
        else:
            return None
        
