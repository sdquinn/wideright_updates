import datetime as dt
from datetime import datetime
import requests
import pandas as pd

# Endpoints
franchises_URL = "https://wideright.app/api/v1/franchises"
picks_URL = "https://www49.myfantasyleague.com/2023/export?TYPE=futureDraftPicks&L=59643&APIKEY=ahFi18iVvuWtx02mPVDHZTEeF7ox&JSON=1"
rosters_URL = "https://wideright.app/api/v1/rosters"
players_url = 'https://www49.myfantasyleague.com/2023/export?TYPE=players&L=59643&APIKEY=&DETAILS=&SINCE=&PLAYERS=&JSON=1'

#Images
dollar_icon = "https://icons.veryicon.com/png/o/business/business-icon-2/money-42.png"
contract_icon = "https://cdn-icons-png.flaticon.com/512/126/126249.png"
player_icon = "https://cdn-icons-png.flaticon.com/512/164/164457.png"

#League Year
cur_month = datetime.now().month
cur_yr = datetime.now().year

if cur_month > 2:
    league_yr = cur_yr
else:
    league_yr = cur_yr-1

#League Data
league_url = 'https://www49.myfantasyleague.com/'+str(league_yr)+'/export?TYPE=league&L=59643&APIKEY=&JSON=1'
r = requests.get(url = league_url)
league = r.json()["league"]
roster_size = int(league["rosterSize"])
salary_cap = float(league["salaryCapAmount"])
contract_cap = 42
max_contract_yrs = 5

#Contract Years Lookup
yr_list = list(range(league_yr, league_yr+max_contract_yrs,1))
contract_yrs = list(range(1,max_contract_yrs+1,1))
zipped_list = list(zip(contract_yrs, yr_list))
cols = ["Contract Length", "Year"]
zipped_df = pd.DataFrame(zipped_list, columns = cols)

# Positional Order
df_mapping = pd.DataFrame({
    'positions': ['QB', 'RB', 'WR', 'TE', 'DEF', 'K'],
})
sort_mapping = df_mapping.reset_index().set_index('positions')

#2023 Holdouts List
    # Generated by https://colab.research.google.com/drive/1fFL2rq3xQ41UD04r7BrwMVQgkDcmzAEq#scrollTo=tDHcz-cvIgkx
holdouts_2023 = ['14073',
 '14840',
 '14127',
 '13633',
 '14223',
 '15290',
 '13404',
 '14208',
 '15797',
 '14059',
 '13424',
 '15308',
 '15237',
 '14071',
 '14104',
 '15289',
 '15753',
 '13156',
 '15331',
 '15238',
 '15254',
 '15282',
 '14845',
 '13632',
 '15762',
 '14858',
 '15240',
 '13418',
 '14857',
 '11938',
 '14838',
 '12650',
 '15716',
 '14239',
 '13646',
 '15288',
 '15708',
 '11679',
 '14778',
 '14835',
 '15284',
 '13113',
 '14080',
 '14087',
 '15711',
 '15789',
 '14974',
 '12652',
 '14102',
 '14109',
 '14802',
 '13635',
 '14136',
 '15258',
 '14803',
 '13630',
 '13622',
 '15293',
 '15261',
 '15505',
 '11675',
 '13129',
 '13153',
 '12447',
 '14783',
 '11674',
 '15721',
 '14105',
 '15733',
 '13593',
 '11247',
 '15253',
 '15751',
 '10738',
 '12678',
 '11680',
 '15255',
 '15889',
 '13623',
 '14832',
 '14779',
 '13610',
 '14797',
 '13157',
 '15287',
 '12611',
 '15715',
 '15271',
 '13726',
 '11678',
 '14841',
 '15281',
 '15259',
 '14017',
 '13629',
 '13164',
 '15754',
 '15755',
 '15779',
 '15256',
 '13671',
 '14777',
 '12186',
 '13319',
 '14833',
 '14848',
 '15798',
 '15766',
 '14113',
 '15757',
 '15717']