from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

cisco4_dict = {"host": "cisco4.lasthop.io", "username": "pyclass", "password": getpass(), "device_type": "cisco_ios"}
cisco4_connect = ConnectHandler(**cisco4_dict)

for dev_cmd in ("sh version", "sh lldp neighbors"):
    print(f'Printing the output of "{dev_cmd}"')
    output = cisco4_connect.send_command(dev_cmd, use_textfsm = True)
    pprint(output)
    print("=" * 60)
    
    if dev_cmd == "sh lldp neighbors":
        print(f'Remote interface is {output[0]["neighbor_interface"]}')

cisco4_connect.disconnect()

