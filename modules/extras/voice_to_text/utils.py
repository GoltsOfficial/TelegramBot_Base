import requests
import os
from dotenv import load_dotenv

load_dotenv()

YANDEX_API_KEY = os.getenv("YANDEX_SPEECHKIT_KEY")
YANDEX_RECOGNIZE_URL = "https://stt.api.cloud.yandex.net/speech/v1/stt:recognize"

def recognize_voice(file_path: str) -> str:
    """
    Отправляем аудиофайл в Yandex SpeechKit и получаем текст.
    """
    headers = {"Authorization": f"Api-Key {YANDEX_API_KEY}"}
    with open(file_path, "rb") as f:
        response = requests.post(
            YANDEX_RECOGNIZE_URL,
            headers=headers,
            files={"file": f},
            params={"lang": "ru-RU", "format": "lpcm", "sampleRateHertz": 48000}
        )
    if response.status_code == 200:
        return response.text.strip()
    else:
        return f"Ошибка распознавания: {response.status_code}"
