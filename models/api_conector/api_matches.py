import requests
import datetime

import configs
import models.api_conector.login as login
from . import api_base_url

api_match_url = f'{api_base_url}/esportes/{login.volei_id}/partidas'

#Não funciona, erro interno
def scheduleMatch(date=None,local='Estadio Olimpico',fase=None):

    headers = {'Authorization': f'Bearer {login.token}','Content-Type': 'application/json'}
    
    current_time = datetime.datetime.now().time().isoformat()
    
    data = {'date':f'{date if date else current_time}', 
            'local':f'{local}', 
            'fase':'teste'
    }

    response = requests.post(api_match_url, headers=headers, data=data)

    match response.status_code:
        case 200:
            print(f'{response.json()}')
        case 401 | 403: 
            error = response.json().get('error')
            print(f"{error}\nErro na comunicação com a API...")
            exit(1)
        case _:
            print(f"Erro não previsto - {response.status_code}")
            #print(f"Mensagem do servidor : {response.text}")
            exit(1)

#Não funciona, erro interno
def getMatchesData():

    headers = {'Authorization': f'Bearer {login.token}','Content-Type': 'application/json'}
    
    response = requests.get(api_match_url, headers=headers)

    match response.status_code:
        case 200:
            country_data = response.json()
            return country_data
        case 401 | 403: 
            error = response.json().get('error')
            print(f"{error}\nErro na comunicação com a API...")
            exit(1)
        case _:
            print(f"Erro não previsto - {response.status_code}")
            #print(f"Mensagem do servidor : {response.text}")
            exit(1)