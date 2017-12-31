import requests, json, datetime, shutil, os
from pytrends.request import TrendReq

homedir = os.path.expanduser("~")
print(homedir)
API_REQ = requests.get("https://api.coinmarketcap.com/v1/ticker/")
AVIAL_CURS = json.loads(API_REQ.text)



# m=0
# for i in AVIAL_CURS:
# 	kw_list = [i["id"]]
# 	pytrends = TrendReq(hl='en-US', tz=360)
# 	trend = pytrends.build_payload(kw_list=kw_list, timeframe='now 7-d')
# 	print(pytrends.interest_over_time())
# 	m+=1
# 	if m>=3:
# 		break

kw_list=["electroneum"]
pytrends = TrendReq(hl='en-US', tz=360)
trend = pytrends.build_payload(kw_list=kw_list, timeframe='now 7-d')
ork = pytrends.interest_over_time()
print(str(ork) + " ork")

ork.electroneum[ork.electroneum == 100 ].index.tolist()