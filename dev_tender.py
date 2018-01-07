import requests, json, datetime, shutil, os, time
from pytrends.request import TrendReq
from pymongo import MongoClient

homedir = os.path.expanduser("~")
print(homedir)
API_REQ = requests.get("https://api.coinmarketcap.com/v1/ticker/")
AVIAL_CURS = json.loads(API_REQ.text)

if not os.path.isfile('config.json'):
	shutil.copy(homedir + '/nasghoul/Dokumente/config.json','.')

with open('config.json','r') as data_file:
	data = json.load(data_file)
	PASSWORD = data['Mongo']['password']
	USERNAME = data['Mongo']['user']
	COLLECTION = data['Mongo']['collection']
	HOST = data['Mongo']['host']

print("username= " +str(USERNAME))

client = MongoClient(HOST,username=USERNAME,password=PASSWORD,authSource=COLLECTION)
# ,authMechanism='SCRAM-SHA-1'
db = client.gtrends

for i in db.gtrends.find():
	print(i)

def initMDB(availables):
	for i in availables:
		time.sleep(30)
		kw_list= [i["id"]]
		

m=0
for i in AVIAL_CURS:
	kw_list = [i["id"]]
	pytrends = TrendReq(hl='en-US', tz=360)
	trend = pytrends.build_payload(kw_list=kw_list, timeframe='now 7-d')
	print(pytrends.interest_over_time())
	m+=1
	if m>=3:
		break

# kw_list=["electroneum"]
# pytrends = TrendReq(hl='en-US', tz=360)
# trend = pytrends.build_payload(kw_list=kw_list, timeframe='now 7-d')
# ork = pytrends.interest_over_time()
# print(str(ork) + " ork")

# ork.electroneum[ork.electroneum == 100 ].index.tolist()