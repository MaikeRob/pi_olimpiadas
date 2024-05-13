import json

from models.api_conector import autenticator

#Carrega as credencias de login
with open('/home/maike/projetos/pi_olimpiadas/models/api_conector/credentials.json','r') as arquivo:
    credentials = json.load(arquivo)

api_url = 'https://olimpiadasiesb-7780607c931d.herokuapp.com/'


autenticator(api_url, credentials['username'], credentials['password'])