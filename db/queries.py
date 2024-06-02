import sqlite3

import configs

def query(query_string, params=None):
    connection = sqlite3.connect('db/aplication_databank.db')
    cursor = connection.cursor()
    
    if params:
        result = cursor.execute(query_string, params)
    else:
        result = cursor.execute(query_string)
    
    result = [row[0] for row in cursor.fetchall()]

    connection.close()
    return result


def getCountries():
    return query("SELECT nome FROM paises")

def getAthelets(country=None, athelet_id=None):
    if athelet_id:
        return query("SELECT nome FROM atletas WHERE _id = ? AND esporte = 'vồlei' ", (athelet_id,))
    elif country:
        return query("SELECT nome FROM atletas WHERE pais = ? AND esporte = 'vôlei' ", (country,))
    else:
        return query("SELECT nome FROM atletas WHERE esporte = 'vôlei' ")
    


