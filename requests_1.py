import requests
import json

response = requests.get('https://api.chucknorris.io/jokes/random')

if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=4))
else:
    print(f"Error al obtener datos: {response.status_code}")