import pprint
import requests
import sys

list_param=sys.argv
card= list_param[1]
r = requests.get('https://lookup.binlist.net/%s' % card, headers={'Accept-Version':'3'})
pprint.pprint(r.json())
