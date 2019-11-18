from scorers import *
from status import *
from leagues import *

request_status()
limit = get_requests_day_count()

print("---------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------")

if limit < 100:
    # get_top_scorers_in_ligue_1_fr_2018()
    # get_top_scorers_in_ligue_1_fr_2019()
    get_all_leagues()
    # get_all_fr_leagues_by_code()



