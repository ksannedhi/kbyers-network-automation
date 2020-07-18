import os
from pprint import pprint
import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

ip_id = input("Input the ID of the IP entry that was made in the previous exercise: ")
url = f"https://netbox.lasthop.io/api/ipam/ip-addresses/{ip_id}/"

token = "Token " + os.getenv("NETBOX_TOKEN")
http_headers = {"Content-Type": "application/json; version=2.4", "accept": "application/json; version=2.4", "authorization": token}

ip_desc = {"address": "192.168.0.102/32", "description": "Description added via a Rest-API call"}
response = requests.put(url, headers = http_headers, verify = False, data = json.dumps(ip_desc))

print(f"Response code: {response.status_code}")
pprint(response.json())
