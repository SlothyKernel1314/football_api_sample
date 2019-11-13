import requests
from headers import *


def get_all_leagues():
    url = "https://server1.api-football.com/leagues"
    response = requests.request("GET", url, headers=HEADERS)
    datas = response.json()
    print(datas)


def get_all_fr_leagues_by_code():
    url = "https://server1.api-football.com/leagues/country/FR"
    response = requests.request("GET", url, headers=HEADERS)
    datas = response.json()
    print(datas)
