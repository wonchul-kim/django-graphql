#!bin/sh

grep -v '^#' /graphql_server/.env
export $(grep -v '^#' /graphql_server/.env | xargs)

python /graphql_server/manage.py makemigrations 
python /graphql_server/manage.py migrate 
python /graphql_server/manage.py runserver ${SERVER_IP}:${SERVER_PORT}