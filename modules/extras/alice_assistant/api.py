import requests
import os
from dotenv import load_dotenv

load_dotenv()

YANDEX_DIALOGS_TOKEN = os.getenv("YANDEX_DIALOGS_TOKEN")

def ask_alice(text: str, user_id: int):
    url = "https://dialogs.yandex.net/api/v1/skills/<SKILL_ID>/invoke"
    headers = {
        "Authorization": f"Bearer {YANDEX_DIALOGS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "version": "1.0",
        "session": {"user_id": str(user_id)},
        "request": {"command": text}
    }
    r = requests.post(url, headers=headers, json=payload)
    if r.status_code == 200:
        return r.json().get("response", {}).get("text", "Извини, Алиса молчит.")
    return "Ошибка соединения с Алисой."
