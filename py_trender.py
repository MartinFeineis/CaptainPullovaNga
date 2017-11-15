from pytrends.request import TrendReq

kw_list = ["ripple"]
pytrends = TrendReq(hl='en-US', tz=360)
trend = pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')
print(trend)
pytrends.interest_over_time()
