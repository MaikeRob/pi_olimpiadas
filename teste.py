from requests import get
from models.api_conector.athletes import getAthletesData

country_data = getAthletesData()

print(country_data)

