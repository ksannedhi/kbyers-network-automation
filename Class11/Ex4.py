import os
import json
from pprint import pprint
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = "https://netbox.lasthop.io/api/ipam/ip-addresses/"
token = "Token " + os.getenv("NETBOX_TOKEN")
http_headers = {"Content-Type": "application/json; version=2.4", "accept": "application/json; version=2.4", "authorization": token}

new_ip = {"address": "192.0.2.102/32"}

response = requests.post(url, headers = http_headers, data = json.dumps(new_ip), verify = False)

print(f'Response code: {response.status_code}')
print()
print("Returned JSON:")
pprint(response.json())
print()

address_id = response.json()["id"]
url = f"https://netbox.lasthop.io/api/ipam/ip-addresses/{address_id}"
response = requests.get(url, headers = http_headers, verify = False)
response = response.json()

print("Newly crerated IP address details:")
pprint(response)

