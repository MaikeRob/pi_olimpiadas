import requests

#Realiza o login na api
def autenticator(url_login, username, password):

    data_login = {
        'username': username,
        'password': password
    }
    response = requests.post(url_login, data=data_login)

    if response.status_code == 200:
        print("Token obtido com sucesso!")
    elif response.status_code == 401:
        error = response.json().get('error')
        print(f"Erro no login: {error}")
    else:
        print("Erro não previsto")


url_login = 'https://olimpiadasiesb-7780607c931d.herokuapp.com/login/token'

username = 'volei'
password = 'volei1234'

autenticator(url_login,username,password)