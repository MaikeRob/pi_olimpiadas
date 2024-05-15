import json

import models.api_conector.login as login

#Carrega as credencias de login
with open('/home/maike/projetos/pi_olimpiadas/models/api_conector/credentials.json','r') as arquivo:
    credentials = json.load(arquivo)

api_url = 'https://olimpiadasiesb-7780607c931d.herokuapp.com/'


login.autenticator(api_url, credentials['username'], credentials['password'])