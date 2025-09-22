import requests

class OneCAPI:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token

    def get_data(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(url, headers=headers)
        return response.json()
