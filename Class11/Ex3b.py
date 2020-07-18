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

list_of_devices = response["results"]

print("-" * 33)
print("List of devices in the inventory:")
for device in list_of_devices:
    print("-" * 33)
    print(device["display_name"])
    print("-" * 9)
    print(f'Location: {device["site"]["name"]}')
    print(f'Vendor: {device["device_type"]["manufacturer"]["name"]}')
    print(f'Status: {device["status"]["label"]}')
    print("-" * 33)

