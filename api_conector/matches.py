import requests
import datetime

import configs
import api_conector.login as login
import api_conector.sports as sports

api_match_url = f'{login.api_base_url}/esportes/{sports.voleibol_id}/partidas'
api_get_matchs_url = f'{login.api_base_url}/esportes/partidas'


def scheduleMatch(date=None,local='Estadio Olimpico do Brasil',fase=None, country1_id=None, country2_id=None):
    print(sports.voleibol_id)

    headers = {'Authorization': f'Bearer {login.token}','Content-Type': 'application/json'}
    
    current_time = datetime.datetime.now().time().isoformat()
    print(current_time)

    data = {
    'date': f'{date if date else current_time}', 
    'local': f'{local}', 
    'fase': f'{fase}',
    'participantes': [
        f'{country1_id}',
        f'{country2_id}'
    ]
    }

    response = requests.post(api_match_url, headers=headers, json=data)

    match response.status_code:
        case 201:
            print(f'Partida Agendada - id : {response.json().get("_id")}')
            match_id = response.json().get('_id')
            return match_id
        case 401 | 403: 
            error = response.json().get('error')
            print(f"{error}\nErro na comunicação com a API...")
            exit(1)
        case _:
            print(f"Erro não previsto - {response.status_code}")
            #print(f"Mensagem do servidor : {response.text}")
            exit(1)


def getMatchesData():

    headers = {'Authorization': f'Bearer {login.token}','Content-Type': 'application/json'}
    
    response = requests.get(api_get_matchs_url, headers=headers)

    match response.status_code:
        case 200:
            matchs_data = response.json()
            return matchs_data
        case 401 | 403: 
            error = response.json().get('error')
            print(f"{error}\nErro na comunicação com a API...")
            exit(1)
        case _:
            print(f"Erro não previsto - {response.status_code}")
            #print(f"Mensagem do servidor : {response.text}")
            exit(1)


def deleteMatch(match_id):

    headers = {'Authorization': f'Bearer {login.token}','Content-Type': 'application/json'}

    api_delete_match_url = f'{api_match_url}?_id={match_id}'

    response = requests.delete(api_delete_match_url, headers=headers)

    match response.status_code:
        case 200:
            print(f'Partida Deletada com sucesso - id : {response.json().get("_id")}')
            match_id = response.json().get('_id')
        case 401 | 403: 
            error = response.json().get('error')
            print(f"{error}\nErro na comunicação com a API...")
            exit(1)
        case 404:
            print("Partida não encontrada - 404")
        case _:
            print(f"Erro não previsto - {response.status_code}")
            #print(f"Mensagem do servidor : {response.text}")
            exit(1)