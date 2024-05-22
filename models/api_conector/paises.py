import configs
import requests

import models.api_conector.login as login
from . import api_base_url

api_country_url = f'{api_base_url}/paises'



def getCountryData():

    headers = {'Authorization': f'Bearer {login.token}'}
    
    response = requests.get(api_country_url, headers=headers)

    if response.status_code == 200:
        country_data = response.json()
        return country_data
    elif response.status_code == 401 or response.status_code == 403:
        error = response.json().get('error')
        print(f"{error}\nErro na comunicação com a API...")
        exit(1)
    else:
        print("Erro não previsto")
        exit(1)
