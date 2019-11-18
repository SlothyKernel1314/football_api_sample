import requests
from headers import *


def get_all_countries():
    url = "https://server1.api-football.com/countries"
    response = requests.request("GET", url, headers=HEADERS)
    datas = response.json()
    print(datas)
