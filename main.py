from scorers import *
from status import *
from leagues import *
from countries import *
from standings import *

request_status()
limit = get_requests_day_count()

print("---------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------")

if limit < 100:
    # get_top_scorers_by_league_id("2")
    # get_all_countries()
    # get_all_leagues()
    # get_league_by_code_and_season("GB", "2018")
    # get_all_country_leagues_by_code("FR")
    get_league_table_by_league_id("4")

else:
    print("No way : limit request per day reached")




