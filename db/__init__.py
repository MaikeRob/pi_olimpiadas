import json
import pandas
import sqlite3

import configs
import api_conector as api
from . import queries

connection = sqlite3.connect('db/aplication_databank.db')

# Criar as tabelas 

connection.executescript('''
DROP TABLE IF EXISTS esportes;
DROP TABLE IF EXISTS atletas;
DROP TABLE IF EXISTS paises;
''')

connection.execute('''
CREATE TABLE esportes (
    _id TEXT PRIMARY KEY NOT NULL,
    nome TEXT UNIQUE NOT NULL,
    coletivo TEXT
)
''')

connection.execute('''
CREATE TABLE paises (
    _id TEXT PRIMARY KEY NOT NULL,
    nome TEXT UNIQUE NOT NULL,
    sigla TEXT NOT NULL,
    continente TEXT NOT NULL
)
''')

connection.execute('''
CREATE TABLE atletas (
    _id TEXT PRIMARY KEY NOT NULL,
    pais_id TEXT NOT NULL,
    pais TEXT,
    esporte_id TEXT,
    esporte TEXT,
    nome TEXT,
    idade TEXT,
    FOREIGN KEY (pais_id) REFERENCES paises(id),
    FOREIGN KEY (esporte_id) REFERENCES esportes(id)
)
''')


#Chama dados
country_data = api.countries.getCountryData()
athletes_data = api.athletes.getAthletesData()
sports_data = api.sports.getSportsData()


#Transforma os dados em um data frame do pandas
country_dataFrame = pandas.DataFrame(country_data)
athletes_dataFrame = pandas.DataFrame(athletes_data)
sports_dataFrame = pandas.DataFrame(sports_data)


#Implementa dados no banco
country_dataFrame.to_sql('paises', connection, if_exists='append', index=False)
athletes_dataFrame.to_sql('atletas', connection, if_exists='append', index=False)
sports_dataFrame.to_sql('esportes', connection, if_exists='append', index=False)


connection.close()