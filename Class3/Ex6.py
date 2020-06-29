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
