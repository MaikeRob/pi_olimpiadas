from models.api_conector.athletes import getAthletesData
from models.api_conector.countries import getCountryData

country_data = getCountryData()
print(country_data)
atletas_data = getAthletesData()



