import requests

#Realiza o login na api
def autenticator(url_login, username, password):

    data_login = {
        'username': username,
        'password': password
    }
    response = requests.post(url_login, data=data_login)

    if response.status_code == 200:
        print(f"Token obtido com sucesso! : {response.json().get('token')}")
    elif response.status_code == 401:
        error = response.json().get('error')
        print(f"Erro no login: {error}")
    elif response.status_code == 403:
        print("403 : Proibido")
    else:
        print("Erro não previsto")

