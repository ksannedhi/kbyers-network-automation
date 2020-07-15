'''Use Netmiko to retrieve 'show run' from the Cisco4 device. Feed this configuration into CiscoConfParse.

Use CiscoConfParse to find all of the interfaces on Cisco4 that have an IP address. Print out the interface name and IP address for each interface.
Your solution should work if there is more than one IP address configured on Cisco4.
For example, if you configure a loopback interface on Cisco4 with an IP address, then your solution should continue to work.
The output from this program should look similar to the following:
$ python confparse_ex6.py 

Interface Line: interface GigabitEthernet0/0/0
IP Address Line:  ip address 10.220.88.23 255.255.255.0'''

from os import path
import yaml
from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse

home_dir = path.expanduser("~")
file_name = path.join(home_dir, ".netmiko.yml")

with open(file_name) as f:
    dev_data = yaml.load(f)

cisco4_dict = dev_data["cisco4"]
cisco4_connect = ConnectHandler(**cisco4_dict)
cisco4_run_config = cisco4_connect.send_command_timing("show run")

cisco4_obj = CiscoConfParse(cisco4_run_config.splitlines())
intf_w_ip = cisco4_obj.find_objects_w_child("interface", childspec = r"^\sip address")

for intf in intf_w_ip:
    print("Interface Line:", intf.text)
    ip_addr = intf.re_search_children(r"ip address")
    print("IP Address Line:", ip_addr[0].text)
    print()
