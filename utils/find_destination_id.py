import requests
import json
import re
from config_data import config

city_url = "https://hotels4.p.rapidapi.com/v2/get-meta-data"
headers = {
    "X-RapidAPI-Key": config.RAPID_API_KEY,
    "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}


def destination_id(city):
    pattern = '<[^>]*>'
    quarystring = {'qiery': city, 'locale': 'en_US', 'currency': 'USD'}
    response = requests.request('GET', city_url, headers=headers, params=querystring)
    data = json.loads(response.text)
    with open('step_1_rome.json', 'w') as rome_file:
        json.dump(data, rome_file, indent=4)
    possible_cities = {}
    for i in data['suggestions'][0]['entities']:
        possible_cities[i['destinationId']] = re.sub(pattern, '', i['caption'])
    return possible_cities
