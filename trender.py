import requests, json, datetime, shutil, os
from pytrends.request import TrendReq

homedir = os.path.expanduser("~")
print(homedir)

# MDB_PASSWD = None
# MDB_USER = None
# MDB = None
# MDB_HOST = None
API_REQ = requests.get("https://api.coinmarketcap.com/v1/ticker/")
AVIAL_CURS = json.loads(API_REQ.text)

# if not os.path.isfile('config.json'):
# 	shutil.copy(homedir + '/nasghoul/Dokumente/config.json','.')

# with open('config.json','r') as data_file:
# 	data = json.load(data_file)
# 	PASSWD = data['password']
# 	USER = data['user']
# 	DATABASE = data['database']
# 	HOST = data['host']
# 	COINS = data['coins']

pytrends = TrendReq(hl='en-US', tz=360)
m=0
for i in AVIAL_CURS:
	kw_list = [i["id"]]
	trend = pytrends.build_payload(kw_list=kw_list, timeframe='now 1-d')
	print(pytrends.interest_over_time())
	m+=1
	if m>=3:
		break
# Interest by Region
interest_by_region_df = pytrends.interest_by_region()
print(interest_by_region_df.head())