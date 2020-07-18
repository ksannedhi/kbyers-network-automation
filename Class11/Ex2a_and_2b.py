'''2a. Using the Python requests library, perform an HTTP GET on the base URL of the NetBox server (https://netbox.lasthop.io/api/).
Ensure that you are not verifying the SSL certificate. Print the HTTP status code, the response text, the JSON response, and the HTTP response headers.
These items can be accessed using the following attributes/methods in the Python-requests Response object:

response.status_code
response.text
response.json()
response.headers

2b. Repeat exercise 2a, except properly construct the HTTP request headers as follows:

http_headers = {}
http_headers["accept"] = "application/json; version=2.4;"

You will need to pass these HTTP headers into your HTTP GET request. Once again print the HTTP status code, the response text, the JSON response, and the HTTP response headers.'''

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
