import requests

response = requests.get("https://www.pontia.tech/")

if response.status_code == 200:
    print("Solicitud exitosa")
    print(response.text)
else:
    print(f"Error en la solicitud: {response.status_code}")