import requests

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
headers = {""}

def query_mistral(prompt):
    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 100, "temperature": 0.7}
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Probar con un mensaje
respuesta = query_mistral("¿Qué es la inteligencia artificial?")
print(respuesta)
