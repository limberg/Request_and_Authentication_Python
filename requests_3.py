import requests
import os

api_key = os.getenv("OPEN_AI_API_TOKEN")

question = ("Dime los tres framekorws principales "
            "basados en Python para desarrolo web backend. " 
            "Responde solo con el nombre de cada uno.")

payload = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role":"user", "content": question}],
    "temperature": 0.3 # Cuanto mas bajo, mas precisa la respuesta
}

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

url = "https://api.openai.com/v1/chat/completions"

try:
    response = requests.post(url, headers=headers, json=payload, timeout=3)
except Exception as e:
    print(f"Error en la solicitud: {e}")
    exit(1) # para salir del programa en caso de error

if response.status_code == 200:
    result = response.json()
    answer = result["choices"][0]["message"]["content"]
    print(f"Respuesta de OpenAI: \n {answer}")
else:
    print(f"Error en la solicitud: {response.status_code} - {response.text}")

