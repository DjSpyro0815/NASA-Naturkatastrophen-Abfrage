import requests
import json

Limit = 500 # das sind unsere Ereignisse
Days = 365  # das ist unser Zeitraum von Tagen
URL = f'https://eonet.sci.gsfc.nasa.gov/api/v2.1/events?limit={Limit}&days={Days}'
r = requests.get(URL)  # so holen wir uns die daten
event_data = r.json()  

with open('events.json','w') as f:
	f.write(json.dumps(event_data, indent=4))

event_list = event_data['events']

for event in event_list:
	print(event['title'])
