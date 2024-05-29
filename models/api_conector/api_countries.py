import configs
import requests

import models.api_conector.login as login
from . import api_base_url

api_country_url = f'{api_base_url}/paises'



def getCountryData():

    headers = {'Authorization': f'Bearer {login.token}','Content-Type': 'application/json'}
    
    response = requests.get(api_country_url, headers=headers)

    match response.status_code:
        case 200:
            country_data = response.json()
            return country_data
        case 401 | 403: 
            error = response.json().get('error')
            print(f"{error}\nErro na comunicação com a API...")
            exit(1)
        case _:
            print("Erro não previsto")
            print(f"Mensagem do servidor : {response.text}")
            exit(1)