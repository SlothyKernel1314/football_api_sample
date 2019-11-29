import requests
from headers import *


def get_league_table_by_league_id(league_id):
    url = "https://server1.api-football.com/leagueTable/" + league_id
    response = requests.request("GET", url, headers=HEADERS)
    datas = response.json()
    print(datas)
