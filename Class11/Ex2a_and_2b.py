from pprint import pprint
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = "https://netbox.lasthop.io/api/"
http_headers = {"accept": "application/json; version = 2.4"}

response = requests.get(url, headers = http_headers, verify = False) #In this statement, 'headers' part is totally optional
print(f"HTTP Status Code: {response.status_code}")
print()
print("Response Text follows:")
pprint(response.text)
print()
print("HTTP Response Headers follow:")
pprint(response.headers)
print()
print("JSON response follows:")
pprint(response.json())

