import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from pprint import pprint

url = "https://netbox.lasthop.io/api"
http_headers = {"accept": "application/json; version = 2.4;"}
response = requests.get(url, headers = http_headers, verify = False)
response = response.json()

pprint(response) #Alternately, use the 'curl -L -s https://netbox.lasthop.io/api --insecure | jq' command.

