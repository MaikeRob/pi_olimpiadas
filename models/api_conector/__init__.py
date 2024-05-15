import json

import models.api_conector.login as login

api_url_base = 'https://olimpiadasiesb-7780607c931d.herokuapp.com'
api_login_url = f'{api_url_base}/login/token'

#Carrega as credencias de login
with open('/home/maike/projetos/pi_olimpiadas/models/api_conector/credentials.json','r') as arquivo:
    credentials = json.load(arquivo)

login.autenticator(api_login_url, credentials['username'], credentials['password'])