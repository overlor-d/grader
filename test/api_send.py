import requests
import json

URL = "http://localhost:5000/submit"

payload = {
    "langage": "C",
    "test_id": "1",
    "user_id": "11",
    "code_path": "./fichierC/exercice_1.c",
    "test_path": "./fichierC/exercice_1_correction.c"
}

headers = {
    "Content-Type": "application/json"
}

try:
    response = requests.post(URL, data=json.dumps(payload), headers=headers)
    print("Requête envoyée.")
    print("Code HTTP :", response.status_code)
    print("Réponse :", response.json())
except Exception as e:
    print("Erreur lors de l'envoi :", str(e))
