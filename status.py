import requests
from headers import *


# Allows API users who do not use RapidApi account to know the status of their subscription
# This endpoint is not taken into account in the daily request count
def request_status():
    url = "https://server1.api-football.com/status"
    response = requests.request("GET", url, headers=HEADERS)
    print(response.text)


def get_requests_day_count():
    url = "https://server1.api-football.com/status"
    response = requests.request("GET", url, headers=HEADERS)
    datas = response.json()
    requests_day_count = datas['api']['status']['requests']
    return requests_day_count
