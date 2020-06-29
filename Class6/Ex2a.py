import yaml
from getpass import getpass
import pyeapi

with open("Ex2a.yml") as f:
    devices = yaml.load(f)

arista4_dict = devices["arista4"]
arista4_dict["password"] = getpass()

connection = pyeapi.client.connect(**arista4_dict)
device = pyeapi.client.Node(connection)
output = device.enable("show ip arp")

ip_mac_list = output[0]["result"]["ipV4Neighbors"]

for arp_entry in ip_mac_list:
    print(f'{arp_entry["address"]} --> {arp_entry["hwAddress"]}')

