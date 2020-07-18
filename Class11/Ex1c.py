'''Use curl to retrieve only the device information for a single device (ID=2 for example). Once again this will require authorization. The API URL for this would be (assuming ID 2):
https://netbox.lasthop.io/api/dcim/devices/2/'''

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import os
from pprint import pprint

url = "https://netbox.lasthop.io/api/dcim/devices/2/"
token = "Token " + os.getenv('NETBOX_TOKEN')
http_headers = {"accept": "application/json; version = 2.4", "authorization": token}
response = requests.get(url, headers = http_headers, verify = False)
response = response.json()

pprint(response) #Alternately, use the 'curl -H "Authorization: Token $NETBOX_TOKEN" https://netbox.lasthop.io/api/dcim/devices/2/ --insecure | jq' command
