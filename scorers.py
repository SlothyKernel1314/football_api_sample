import requests
from headers import *


def get_top_scorers_by_league_id(league_id):
    url = "https://server1.api-football.com/topscorers/" + league_id
    response = requests.request("GET", url, headers=HEADERS)
    datas = response.json()
    print(datas)
    print("\n\n")
    print("rank *** name *** team *** goals (s.p.) *** assists *** matchs (ratio) *** minutes per goal ")
    rank = 1
    for player in datas['api']['topscorers']:
        player_first_name = player['firstname']
        player_last_name = player['lastname']
        player_team_name = player['team_name']
        player_goals = str(player['goals']['total'])
        player_penalty_success = str(player['penalty']['success'])
        player_assists = str(player['goals']['assists'])
        player_matches_count = str(player['games']['appearences'])
        player_goals_per_games = str(round(int(player_goals) / int(player_matches_count), 2))
        player_minutes_per_goal = str(round(int(player['games']['minutes_played'] / int(player_goals)), 2))
        result = str(rank) + " *** " + player_first_name + " " + player_last_name + " *** " + player_team_name \
                 + " *** " + player_goals + " (" + player_penalty_success + "p.) *** " + player_assists \
                 + " *** " + player_matches_count + " (" + player_goals_per_games + "b/m) *** " \
                 + player_minutes_per_goal + "'"
        print(result)
        rank += 1


