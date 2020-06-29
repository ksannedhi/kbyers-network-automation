import pyeapi
from getpass import getpass

arista3_dict = {"host": "arista3.lasthop.io", "username": "pyclass", "password": getpass(), "transport": "https", "port": 443}

connection = pyeapi.client.connect(**arista3_dict)
device = pyeapi.client.Node(connection)
output = device.enable("sh ip arp")
ip_mac_list = output[0]["result"]["ipV4Neighbors"]

for arp_entry in ip_mac_list:
    print(f'{arp_entry["address"]} --> {arp_entry["hwAddress"]}')
