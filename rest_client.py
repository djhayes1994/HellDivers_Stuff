import requests
# import json

BASE_URL = "https://helldiverstrainingmanual.com/api/v1/"

class client:
    def __init__(self) -> None:
        pass
    def request(self,endpoint=None,method="GET"):
        method = method.lower()
        endpoint = endpoint

        if endpoint is not None:

            url = BASE_URL+endpoint
            headers = {"Content-Type": "application/json"}
            if method == "get":
                try:
                    response = requests.get(url)
                    return response.json()
                except:
                    return f"ERROR: Something went wrong." 
            else:
                return f"ERROR: Method of '{method.upper()}' is not supported by the API." 
        else:
            return f"Endpoint cannot be none."
        