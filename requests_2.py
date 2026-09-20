import requests

latitude = 40.4154
longitude = -3.7074

# URL (Open-Meteo API)
url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}"
        f"&current_weather=true"
)

# Execute request:
response = requests.get(url)

if(response.status_code == 200):
    data = response.json()
    weather = data['current_weather']
    print(f" Temperatura:{weather['temperature']}°C, Velocidad del viento: {weather['windspeed']} km/h, Dirección del viento: {weather['winddirection']}°")
else:
    print(f"Error al obtener los datos metereologicos: {response.status_code}")