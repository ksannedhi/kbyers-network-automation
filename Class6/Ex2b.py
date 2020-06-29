from Ex2b_my_funcs import yaml_load, print_arp_entries
from getpass import getpass
import pyeapi

devices = yaml_load()
arista4_dict = devices["arista4"]
arista4_dict["password"] = getpass()

connection = pyeapi.client.connect(**arista4_dict)
device = pyeapi.client.Node(connection)
output = device.enable("show ip arp")

print_arp_entries(output[0]["result"]["ipV4Neighbors"])
