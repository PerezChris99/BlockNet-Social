import requests

class DeFiContract:
    def __init__(self, canister_id, url):
        self.canister_id = canister_id
        self.url = url

    def call_method(self, method, params):
        response = requests.post(f"{self.url}/api/v2/canister/{self.canister_id}/{method}", json=params)
        return response.json()
