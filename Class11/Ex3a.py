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

