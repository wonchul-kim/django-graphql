import graphene
from graphene_django import DjangoObjectType 
from athena.models import TrainExpDB, TrainExpServerInfoDB 

class TrainExpServerInfoType(DjangoObjectType):
    class Meta:
        model = TrainExpServerInfoDB 
        fields = ('id', 'train_exp', 'server_host_name', 'server_ip', 'container_name', 'description')
        
class CreateTrainExpServerInfo(graphene.Mutation):
    class Arguments:
        train_exp = graphene.Int(required=True)
        server_host_name = graphene.String(required=False)
        server_ip = graphene.String(required=False)
        container_name = graphene.String(required=False)
        description = graphene.String(required=False)
        
    train_exp_server_info = graphene.Field(TrainExpServerInfoType)
    msg = graphene.String() 
    
    @classmethod 
    def mutate(cls, self, info, train_exp, server_host_name="", server_ip="", container_name="", description=""):
        if TrainExpDB.objects.filter(id=train_exp):
            train_exp_db_obj = TrainExpDB.objects.get(id=train_exp)
            train_exp_server_info_db = TrainExpServerInfoDB(train_exp=train_exp_db_obj, server_host_name=server_host_name, \
                                                server_ip=server_ip, container_name=container_name, description=description)
            train_exp_server_info_db.save()

            return CreateTrainExpServerInfo(train_exp_server_info=train_exp_server_info_db, msg="Successfully added!")
        else:
            return None
        

       