''' Use an HTTP DELETE and Python-requests to delete the IP address object that you just created. Remember to reference the ID of your object.'''

import os
import json
from pprint import pprint
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

ip_id = input("ID of the IP entry you want to delete: ")
url = f'https://netbox.lasthop.io/api/ipam/ip-addresses/{ip_id}/'
token = "Token " + os.getenv("NETBOX_TOKEN")
http_headers = {"Content-Type": "application/json; version=2.4", "accept": "application/json; version=2.4", "authorization": token}

response = requests.delete(url, headers = http_headers, verify = False)

print(f"Response code: {response.status_code}")
pprint(response.json())
