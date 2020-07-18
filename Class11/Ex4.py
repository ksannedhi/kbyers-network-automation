'''4a. Using an HTTP POST and the Python-requests library, create a new IP address in NetBox. This IP address object should be a /32 from the 192.0.2.0/24 documentation block.
Print out the status code and the returned JSON.

The HTTP headers for this request should look as follows:

http_headers = {}
http_headers["Content-Type"] = "application/json; version=2.4;"
http_headers["accept"] = "application/json; version=2.4;"
http_headers["Authorization"] = f"Token {token}"

The URL for the HTTP POST is:

https://netbox.lasthop.io/api/ipam/ip-addresses/

The JSON payload data for this request should be similar to the following:

data = {"address": "192.0.2.100/32"}

4b. Using the response data from the HTTP POST that created the IP address entry in exercise 4a, capture the "id" of the newly created IP address object.
Using this ID, construct a new URL. Use this new URL and the HTTP GET method to retrieve only the API information specific to this IP address.
Your IP address URL should be of the following form:
https://netbox.lasthop.io/api/ipam/ip-addresses/{address_id}/

where {address_id} is the ID of the object that you just created.

Pretty print the response.json() data from this HTTP GET. Please note the ID of the address object that you just created.'''

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
