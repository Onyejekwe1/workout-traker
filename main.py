import requests
from datetime import datetime

from requests.auth import HTTPBasicAuth

NUTRITION_IX_APP_ID = "YOU NUTRITIONIX APP ID"
NUTRITION_IX_APP_KEY = "YOU NUTRITIONIX APP KEY"

NUTRITION_IX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_USERNAME = "YOUR SHEETY USER NAME"
SHEETY_PROJECT_NAME = "YOUR SHEETY PROJECT NAME"
SHEETY_SHEET_NAME = "YOUR SHEETY SHEET NAME"
SHEETY_url = f"https://api.sheety.co/{SHEETY_USERNAME}/{SHEETY_PROJECT_NAME}/{SHEETY_SHEET_NAME}"

headers = {
    "x-app-id": NUTRITION_IX_APP_ID,
    "x-app-key": NUTRITION_IX_APP_KEY,
    "Content-Type": "application/json"
}

query = input("Tell me what exercise you did today: ")

nutrix_body = {
    "query": query,
    "gender": "female",
    "weight_kg": 110,
    "height_cm": 175,
    "age": 28
}

response = requests.post(url=NUTRITION_IX_ENDPOINT, json=nutrix_body, headers=headers)

exercises = response.json()["exercises"]
exercise = exercises[0]["name"].title()
duration = exercises[0]["duration_min"]
calories_burned = exercises[0]["nf_calories"]
meters = exercises[0]["met"]
now = datetime.now()
print(exercises)

sheety_body = {
    "workout": {
        "date": now.strftime("%d/%m/%Y"),
        "time": now.strftime("%H:%M:%S"),
        "exercise": exercise,
        "duration": duration,
        "calories": calories_burned
    }
}

sheet_response = requests.post(url=SHEETY_url, json=sheety_body, auth=HTTPBasicAuth('ionyejekwe', 'Laporta1.'))

print(sheet_response.json())