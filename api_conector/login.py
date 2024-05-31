import configs
import requests

volei_id = "6601ecda7d406070201176ab"
api_base_url = 'https://olimpiadasiesb-7780607c931d.herokuapp.com'
api_login_url = f'{api_base_url}/login/token'

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

