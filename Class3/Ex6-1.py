from os import path
import yaml
from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse

file_dir = path.expanduser("~")
file_name = path.join(file_dir, ".netmiko.yml")

with open(file_name) as f:
    dev_data = yaml.load(f)

cisco4_dict = dev_data["cisco4"]
cisco4_connect = ConnectHandler(**cisco4_dict)

sh_run = cisco4_connect.send_command("sh run")

sh_run_lines = CiscoConfParse(sh_run.splitlines())
intf_data = sh_run_lines.find_objects_w_child(parentspec = r'^interface', childspec = r'^\s+ip address') #Writing "parentspec" is optional.

for intf in intf_data:
    print(f'Interface Line: {intf.text}')
    ip_addr_list = intf.re_search_children(r'ip address')
    for ip in ip_addr_list: #This for loop method is useful when you have multiple IP addresses per interface - ipv6 case.
        print(f"IP Address Line: {(ip.text).strip()}")
    print("=" * 60)

