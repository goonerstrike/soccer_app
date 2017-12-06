mport requests
import urllib2
import json


###################################### football-data.org API
# API Key 1310374de6494d8dbe31e7f84aa85f23



# Function to retrieve all competitions
def get_leagues():    
    url = 'https://api.football-data.org/v1/competitions'
    headers = {'Authorization': 'Bearer 1310374de6494d8dbe31e7f84aa85f23'}
    r = requests.get(url, headers=headers, verify=False)
    competitions = r.json()
    return competitions

epl = get_epl()
epl_fixtures = epl["_links"]["fixtures"]

for i in epl:
    print i["caption"]

