import requests
from headers import *


def get_all_leagues():
    url = "https://server1.api-football.com/leagues"
    response = requests.request("GET", url, headers=HEADERS)
    datas = response.json()
    print(datas)


def get_league_by_code_and_season(country, season):
    url = "https://server1.api-football.com/leagues/country/" + country + "/" + season
    response = requests.request("GET", url, headers=HEADERS)
    datas = response.json()
    print(datas)


def get_all_country_leagues_by_code(code):
    url = "https://server1.api-football.com/leagues/country/" + code
    response = requests.request("GET", url, headers=HEADERS)
    datas = response.json()
    print(datas)



