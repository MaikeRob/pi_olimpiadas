import configs
import requests

import models.api_conector.login as login

authentication_done = False
token = None

#Realiza o login na api
def autenticator(url_login, username, password):

    data_login = {
        'username': username,
        'password': password
    }
    response = requests.post(url_login, data=data_login)

    if response.status_code == 200:
        print(f"Token obtido com sucesso! : {response.json().get('token')}")
        authentication_done = True
        return response.json().get('token')
    elif response.status_code == 401:
        error = response.json().get('error')
        print(f"Erro no login: {error}")
        exit(1)
    elif response.status_code == 403:
        error = response.json().get('error')
        print(f"Proibido : {error}")
        exit(1)
    else:
        print("Erro não previsto")
        exit(1)

