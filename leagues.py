import requests
from headers import *


def get_all_leagues():
    url = "https://server1.api-football.com/leagues"
    response = requests.request("GET", url, headers=HEADERS)
    datas = response.json()
    print(datas)


# France
def get_all_fr_leagues_by_code():
    url = "https://server1.api-football.com/leagues/country/FR"
    response = requests.request("GET", url, headers=HEADERS)
    datas = response.json()
    print(datas)


# England / Great Britain
def get_all_gb_leagues_by_code():
    url = "https://server1.api-football.com/leagues/country/GB"
    response = requests.request("GET", url, headers=HEADERS)
    datas = response.json()
    print(datas)


# Spain
def get_all_es_leagues_by_code():
    url = "https://server1.api-football.com/leagues/country/ES"
    response = requests.request("GET", url, headers=HEADERS)
    datas = response.json()
    print(datas)


# Germany
def get_all_de_leagues_by_code():
    url = "https://server1.api-football.com/leagues/country/DE"
    response = requests.request("GET", url, headers=HEADERS)
    datas = response.json()
    print(datas)


# Italy
def get_all_it_leagues_by_code():
    url = "https://server1.api-football.com/leagues/country/IT"
    response = requests.request("GET", url, headers=HEADERS)
    datas = response.json()
    print(datas)



