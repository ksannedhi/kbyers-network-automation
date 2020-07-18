'''Retrieve a list of all the devices in NetBox. This will require authentication. As in the previous task, create your headers manually and pass them into your request.
In order to perform the NetBox authentication, you should do the following:

import os
# Set the token based on the NETBOX_TOKEN environment variable
token = os.environ["NETBOX_TOKEN"]

Then add the following key to your HTTP Headers:

http_headers["Authorization"] = f"Token {token}"

From this returned data structure (the NetBox "/api/dcim/devices/"), print out all of the device "display_names". Note, the response.json() will contain a "results" key.
This "results" key will refer to a list of dictionaries. These dictionaries will contain information about each one of the devices in NetBox.'''

import os
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from pprint import pprint

url = "https://netbox.lasthop.io/api/dcim/devices"
token = "Token " + os.environ["NETBOX_TOKEN"] #Alternative to os.getenv("NETBOX_TOKEN")
http_headers = {"accept": "application/json; version = 2.4", "authorization": token}
response = requests.get(url, headers = http_headers, verify = False)
response = response.json()

devices = response["results"]

print("List of devices in the inventory:")
for device in devices:
    print(device["display_name"])
