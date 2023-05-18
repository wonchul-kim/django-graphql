from django.urls import path 
from graphene_django.views import GraphQLView 
from graphql_playground.views import GraphQLPlaygroundView 

# urlpatterns = [
#     path("graphql/", GraphQLView.as_view(graphiql=True)),
# ]

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('graphql-playground/', csrf_exempt(GraphQLPlaygroundView.as_view(endpoint="/graphql/"))),
]