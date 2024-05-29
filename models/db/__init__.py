import json
import pandas
import sqlite3

import configs
from models.api_conector import api_athletes, api_countries

#Chama dados
country_data = api_countries.getCountryData()
#athletes_data = api_athletes.getAthletesData()

country_dataFrame = pandas.DataFrame(country_data)
#athletes_dataFrame = pandas.DataFrame(athletes_data)

#Implementa dados no banco
connection = sqlite3.connect('models/db/aplication_databank.db')

country_dataFrame.to_sql('countries', connection, if_exists='replace', index=False)

connection.close