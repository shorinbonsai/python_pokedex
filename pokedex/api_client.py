import requests
from pokecache import Cache

class Client:
    base_url = "https://pokeapi.co/api/v2/"

    def __init__(self, cache_interval):
        self.cache = Cache(cache_interval)
        self.http_client = requests.Session()
        self.http_client.timeout = 60  # Timeout in seconds