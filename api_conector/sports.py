import configs
import requests

import api_conector.login as login

api_sports_url = f'{login.api_base_url}/esportes'


def getSportsData():

    headers = {'Authorization': f'Bearer {login.token}','Content-Type': 'application/json'}
    
    response = requests.get(api_sports_url, headers=headers)

    match response.status_code:
        case 200:
            sports_data = response.json()
            return sports_data
        case 401 | 403: 
            error = response.json().get('error')
            print(f"{error}\nErro na comunicação com a API...")
            exit(1)
        case _:
            print(f"Erro não previsto - {response.status_code}")
            #print(f"Mensagem do servidor : {response.text}")
            exit(1)

def getVoleiID():

    print(login.token)
    headers = {'Authorization': f'Bearer {login.token}','Content-Type': 'application/json'}
    
    response = requests.get(api_sports_url, headers=headers)

    match response.status_code:
        case 200:
            sports_data = response.json()
            for sport in sports_data:
                if sport.get('nome') == 'vôlei':
                    return sport.get('_id')
            print("Esporte 'vôlei' não encontrado.")
            return None
        case 401 | 403: 
            error = response.json().get('error')
            print(f"{error}\nErro na comunicação com a API...")
            exit(1)
        case _:
            print(f"Erro não previsto - {response.status_code}")
            #print(f"Mensagem do servidor : {response.text}")
            exit(1)

voleibol_id = None
