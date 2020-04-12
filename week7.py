import requests
from pprint import pprint
crime_url_template = 'https://data.police.uk/api/crimes-street/all-crime?lat={lat}&lng={lng}&date={data}'
my_latitude = '51.52369'
my_longitude = '-0.0395857'
my_date = '2018-11'
crime_url = crime_url_template.format(lat = my_latitude,
	lng = my_longitude,
	data = my_date)
resp = requests.get(crime_url)
if resp.ok:
	crimes = resp.json()
else:
	print(resp.reason)
pprint(crimes)
