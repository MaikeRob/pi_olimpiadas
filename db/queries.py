import sqlite3

import configs

def query(query_string, params=None):
    connection = sqlite3.connect('db/aplication_databank.db')
    cursor = connection.cursor()
    
    if params:
        result = cursor.execute(query_string, params)
    else:
        result = cursor.execute(query_string)
    
    rows = cursor.fetchall()
    if len(rows) == 1:  
        result = rows[0][0]  
    else:
        result = [row[0] for row in rows]  
        
    connection.close()
    return result


def getCountrieID(countrie_name):
    return query("SELECT _id FROM paises WHERE nome = ?", (countrie_name,))

def getCountrie(countrie_id):
    return query("SELECT nome FROM paises WHERE _id = ?", (countrie_id,))

def getCountries():
    return query("SELECT nome FROM paises")

def getAthelets(country=None, athelet_id=None):
    if athelet_id:
        return query("SELECT nome FROM atletas WHERE _id = ? AND esporte = 'vồlei' ", (athelet_id,))
    elif country:
        return query("SELECT nome FROM atletas WHERE pais = ? AND esporte = 'vôlei' ", (country,))
    else:
        return query("SELECT nome FROM atletas WHERE esporte = 'vôlei' ")
    


