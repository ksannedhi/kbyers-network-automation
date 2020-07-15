'''Define an Arista device in an external YAML file (use arista4.lasthop.io for the device).
In your YAML file, make sure the key names exactly match the names required for use with pyeapi and the connect() method.
In other words, you should be able to execute 'connect(**device_dict)' where device_dict was retrieved from your YAML file.
Do not store the lab password in this YAML file, instead set the password using getpass() in your Python program.
Using this Arista device information stored in a YAML file, repeat the 'show ip arp' retrieval using pyeapi.
Once again, from this ARP table data, print out a mapping of all of the IP addresses and their corresponding MAC addresses.'''

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
