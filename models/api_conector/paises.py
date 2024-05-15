import requests

from . import api_base_url

api_country_url = f'{api_base_url}/paises'

def getCountryData():
    
    response = requests.get(api_country_url)

    if response.status_code == 200:
        country_data = response.json()
        return country_data
    elif response.status_code == 401:
        error = response.json().get('error')
        print(error)
        return
    elif response.status_code == 403:
        error = response.json().get('error')
        print(error)
        return
    else:
        print("Erro não previsto")


    return country_data
