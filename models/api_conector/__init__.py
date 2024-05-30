import json

from models.api_conector import login, countries, matches, athletes
import configs


#Carrega as credencias de login
with open('models/api_conector/credentials.json','r') as arquivo:
    credentials = json.load(arquivo)

if not login.authentication_done:
    login.token = login.autenticator(login.api_login_url, credentials['username'], credentials['password'])
    login.authenticatior_done = True
else:
    pass
    