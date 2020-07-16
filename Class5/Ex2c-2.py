'''Use Netmiko to push the configurations generated in exercise 2b to the nxos1 device and to the nxos2 device, respectively.
Verify you are able to ping between the devices and also verify that the BGP session reaches the established state.
Note, you might need to use an alternate interface besides Ethernet 1/1 (you can use either Ethernet 1/1, 1/2, 1/3, or 1/4).
Additionally, you might need to use a different IP network (to avoid conflicts with other students). Your autonomous system should remain 22, however.
For this exercise you should store your Netmiko connection dictionaries in an external file named my_devices.py and should import nxos1, and nxos2 from that external file.
Make sure that you use getpass() to enter the password in for these devices (as opposed to storing the definitions in the file).'''

from my_devices_1 import nxos1, nxos2
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from netmiko import ConnectHandler

env = Environment(undefined = StrictUndefined)
env.loader = FileSystemLoader(".")

interface = "Ethernet1/3"
as_num = 22
nxos1_vars = {"intf_name": interface, "ip_addr": "10.1.200.1", "net_mask": 24, "local_as": as_num, "remote_as": as_num}
nxos2_vars = {"intf_name": interface, "ip_addr": "10.1.200.2", "net_mask": 24, "local_as": as_num, "remote_as": as_num}

nxos1_vars["neighbor_ip"] = nxos2_vars["ip_addr"]
nxos2_vars["neighbor_ip"] = nxos1_vars["ip_addr"]

nxos1_vars["device_dict"] = nxos1
nxos2_vars["device_dict"] = nxos2

for nxos_vars in (nxos1_vars, nxos2_vars):
    nxos_dict = nxos_vars.pop("device_dict")
    t = env.get_template("Ex2b-1.j2")
    config = t.render(nxos_vars)
    config_lines = [line.strip() for line in config.splitlines()]
    nxos_connect = ConnectHandler(**nxos_dict)
    cmd_output = nxos_connect.send_config_set(config_lines)
    nxos_connect.disconnect()
    print(cmd_output)
