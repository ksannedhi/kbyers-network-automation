'''Use Netmiko to push the configurations generated in exercise 2b to the nxos1 device and to the nxos2 device, respectively.
Verify you are able to ping between the devices and also verify that the BGP session reaches the established state.
Note, you might need to use an alternate interface besides Ethernet 1/1 (you can use either Ethernet 1/1, 1/2, 1/3, or 1/4).
Additionally, you might need to use a different IP network (to avoid conflicts with other students). Your autonomous system should remain 22, however.

For this exercise you should store your Netmiko connection dictionaries in an external file named my_devices.py and should import nxos1, and nxos2 from that external file.
Make sure that you use getpass() to enter the password in for these devices (as opposed to storing the definitions in the file).'''

from my_devices import nxos1_dict, nxos2_dict
from netmiko import ConnectHandler
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined = StrictUndefined)
env.loader = FileSystemLoader(".")

as_num = 22
nxos1_vars = {"nxos_int": "Ethernet1/1", "nxos_ip": "10.1.100.1", "nxos_subnet": 24, "nxos_local_as": as_num, "nxos_remote_as": as_num}
nxos2_vars = {"nxos_int": "Ethernet1/1", "nxos_ip": "10.1.100.2", "nxos_subnet": 24, "nxos_local_as": as_num, "nxos_remote_as": as_num}

nxos1_vars["nxos_peer_ip"] = nxos2_vars["nxos_ip"]
nxos2_vars["nxos_peer_ip"] = nxos1_vars["nxos_ip"]

nxos1_dict["j2_vars"] = nxos1_vars
nxos2_dict["j2_vars"] = nxos2_vars

for device_dict in (nxos1_dict, nxos2_dict):
    j2_vars = device_dict.pop("j2_vars")
    t = env.get_template("Ex2b.j2")
    j2_op = t.render(j2_vars)
    j2_op_lines = [line.strip() for line in j2_op.splitlines()]
 
    nxos_connect = ConnectHandler(**device_dict)
    nxos_cmd_op = nxos_connect.send_config_set(j2_op_lines)
    nxos_connect.disconnect()
    print(nxos_cmd_op)
