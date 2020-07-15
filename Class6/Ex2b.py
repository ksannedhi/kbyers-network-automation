'''Create a Python module named 'Ex2b_my_funcs.py'. In this file create two functions: function1 should read the YAML file you created in exercise 2a and return the corresponding data structure;
function2 should handle the output printing of the ARP entries (in other words, create a separate function that handles all printing to standard out of the 'show ip arp' data).
Create a new Python program based on exercise2a except the YAML file loading and the output printing is accomplished using the functions defined in my_funcs.py.'''

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
