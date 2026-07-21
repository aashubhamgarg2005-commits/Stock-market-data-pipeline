import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import json

class BaseClient:
    def __init__(self,base_url,api_key=None,timeout=30):
        self.base_url = base_url
        self.api_key = api_key
        self.timeout = timeout
        self.session = requests.session()
        retry = Retry(
            total = 3,
            backoff_factor = 1,
            status_forcelist = [429,500,502,503,504],
            allowed_methods = ["GET","POST"]
        )

        adepter = HTTPAdapter(max_retries=retry)
        self.session.mount("https://",adapter=adepter)
        self.session.mount("http:/",adapter=adepter)
        

    def get_request(self,endpoint:str,params=None):
        if params is None:
            params = {}

        if self.api_key:
            params["token"] = self.api_key
            url = f"{self.base_url}{endpoint}"
        try:
            response = self.session.get(
                url=url,
                params=params,
                timeout= self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            raise Exception("Request Timeout")
        except requests.exceptions.HTTPError as e:
            raise Exception(f"HTTP Error: {e}")
        except requests.exceptions.RequestException as e:
            raise Exception(f"Request Failed: {e}")
