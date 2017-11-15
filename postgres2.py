import requests, psycopg2, json, datetime, shutil, os
homedir = os.path.expanduser("~")
print(homedir)

PASSWD = None
USER = None
DB = None
HOST = None
API_REQ = requests.get("https://api.coinmarketcap.com/v1/ticker/")
AVIAL_CURS = json.loads(r.text)

if not os.path.isfile('config.json'):
	shutil.copy(homedir + '/nasghoul/Dokumente/config.json','.')

with open('config.json','r') as data_file:
	data = json.load(data_file)
	PASSWD = data['password']
	USER = data['user']
	DATABASE = data['database']
	HOST = data['host']
	COINS = data['coins']

def comp_coins ():
	"""compare the currencies returned by the api with the ones in the config File"""
	for i in AVIAL_CURS["id"]:
		if i not in COINS:
			COINS.append()

def get_ids ():
	"""create tables"""
	conn = psycopg2.connect(host=HOST,dbname=DATABASE, user=USER ,password=PASSWD)
	cur = conn.cursor()
	for i in COINS:
		cid = str(i.replace("-","_"))
		SQL = """CREATE TABLE IF NOT EXISTS {} ( rank INT, price_usd DECIMAL, price_btc DECIMAL, day_volume_usd DECIMAL, 
				market_cap_usd DECIMAL, total_supply DECIMAL, percent_change_1h DECIMAL, percent_change_24h DECIMAL, percent_change_7d DECIMAL, 
				last_updated TIMESTAMP WITH TIME ZONE)""".format(("n"+cid))
		cur.execute(SQL)
		conn.commit()


def ins_values():
	""""populate database with actual values"""
	conn = psycopg2.connect(host=HOST,dbname=DATABASE, user=USER ,password=PASSWD)
	cur = conn.cursor()
	for i in AVIAL_CURS:
		cid = str(i["id"].replace("-","_"))
		ts = datetime.datetime.fromtimestamp(int(i['last_updated']))
		print(cid)
		SQL = """INSERT INTO {} ( rank, price_usd, price_btc, day_volume_usd, market_cap_usd, total_supply,
			percent_change_1h, percent_change_24h, percent_change_7d, last_updated)
			VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""".format(("n"+cid))
		data = (i["rank"], i["price_usd"], i["price_btc"], i["24h_volume_usd"], i["market_cap_usd"], i["total_supply"], i["percent_change_1h"], i["percent_change_24h"],
			i["percent_change_7d"], ts)
		print(data)
		cur.execute(SQL, data)
		conn.commit()

get_ids()
ins_values()
