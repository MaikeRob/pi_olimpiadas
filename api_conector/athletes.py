import requests

import configs
import api_conector.login as login


api_athlete_url = f'{login.api_base_url}/atletas'

def getAthletesData():

    headers = {'Authorization': f'Bearer {login.token}','Content-Type': 'application/json'}

    response = requests.get(api_athlete_url, headers=headers)

    match response.status_code:
        case 200:
            athletes_data = response.json()
            return athletes_data
        case 401 | 403: 
            error = response.json().get('error')
            print(f"{error}\nErro na comunicação com a API...")
            exit(1)
        case _:
            #print(f"Erro não previsto - {response.status_code}")
            print(f"Mensagem do servidor : {response.text}")
            exit(1)

def registerAthlete(nome, idade):

    api_register_athlete_url = f'{login.api_base_url}/{id_pais}/{id_esporte}'

    headers = {'Authorization': f'Bearer {login.token}','Content-Type': 'application/json'}

    response = requests.post(api_register_athlete_url, headers=headers)