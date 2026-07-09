import requests
from utils.logger import LOGGER

class BaseClient:
    def __init__(self, base_url, api_key):
        self.api_key = api_key
        self.api_url = base_url.rstrip('/')

    def get_request(self, endpoint: str, params: dict = None):
        if params is None:
            params = {}

        params["token"] = self.api_key
        endpoint = endpoint.lstrip('/')
        url = f"{self.api_url}/{endpoint}"

        try:
            response = requests.get(url=url,
                                    params=params,
                                    timeout=10)
            response.raise_for_status()
            return response.json()
        

        except requests.exceptions.RequestException as e:
            LOGGER.error(f"API Error: {e}")
            return None