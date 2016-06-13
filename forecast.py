import requests
import json
import pprint
from ipify import get_ip

def whereami():
    r = requests.get('https://freegeoip.net/json/' + get_ip())
    if r.ok:
        j = r.json() 
        state_code = j['region_code']
        city = j['city']
        return {'state':state_code, 'city':city}
    else:
        print('No internet connection')

loc = whereami()
wunderground_key = '64bff5ef1e41bc7c'
r = requests.get('http://api.wunderground.com/api/' + wunderground_key
        + '/geolookup/conditions/q/' + loc['state'] + '/' + loc['city'] + '.json')
if r.ok:
    j = r.json()
    output = str(j['current_observation']['temp_f']) + 'F, '
    output += j['location']['city'] + ', ' + j['location']['state']
    print(output)
else:
    print('No internet connection')
