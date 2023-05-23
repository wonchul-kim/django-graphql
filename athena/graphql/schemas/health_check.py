import graphene
from graphene_django import DjangoObjectType 
from athena.models import HealthCheckDB 

class HealthCheckType(DjangoObjectType):
    class Meta:
        model = HealthCheckDB 
        fields = ('id', 'health')

class CreateHealthCheck(graphene.Mutation):
    health_check = graphene.Field(HealthCheckType)
    
    @classmethod 
    def mutate(cls, self, info):
        health_check_db = HealthCheckDB(health=True)
        health_check_db.save()
        
        return CreateHealthCheck(health_check=health_check_db)
