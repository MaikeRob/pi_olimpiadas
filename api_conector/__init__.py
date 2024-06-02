import json

from api_conector import login, countries, matches, athletes, sports
import configs

from api_conector import login
#Carrega as credencias de login

with open('api_conector/credentials.json','r') as arquivo:
    credentials = json.load(arquivo)

#Realiza o login
if not login.authentication_done:
    login.token = login.autenticator(login.api_login_url, credentials['username'], credentials['password'])
    login.authenticatior_done = True
    credentials['token'] = login.token
    with open('api_conector/credentials.json', 'w', encoding='utf-8') as arquivo:
        json.dump(credentials, arquivo, ensure_ascii=False, indent=4)
        
else:
    pass
