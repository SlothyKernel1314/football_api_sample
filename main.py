from scorers import *
from status import *
from leagues import *
from countries import *

request_status()
limit = get_requests_day_count()

print("---------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------")

if limit < 100:
    get_top_scorers_by_league_id("2")
    # get_all_countries()
    # get_all_leagues()
    # get_league_by_code_and_season("GB", "2018")
    # get_all_fr_leagues_by_code()
    # get_all_gb_leagues_by_code()
    # get_all_es_leagues_by_code()
    # get_all_de_leagues_by_code()
    # get_all_it_leagues_by_code()

else:
    print("No way : limit request per day reached")




