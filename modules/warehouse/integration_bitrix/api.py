import requests

class Bitrix24API:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def call_method(self, method, params=None):
        url = f"{self.webhook_url}/{method}"
        response = requests.post(url, data=params)
        return response.json()
