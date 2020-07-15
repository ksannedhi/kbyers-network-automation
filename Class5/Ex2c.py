'''Use Netmiko to push the configurations generated in exercise 2b to the nxos1 device and to the nxos2 device, respectively.
Verify you are able to ping between the devices and also verify that the BGP session reaches the established state.
Note, you might need to use an alternate interface besides Ethernet 1/1 (you can use either Ethernet 1/1, 1/2, 1/3, or 1/4).
Additionally, you might need to use a different IP network (to avoid conflicts with other students). Your autonomous system should remain 22, however.

For this exercise you should store your Netmiko connection dictionaries in an external file named my_devices.py and should import nxos1, and nxos2 from that external file.
Make sure that you use getpass() to enter the password in for these devices (as opposed to storing the definitions in the file).'''

from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from netmiko import ConnectHandler
from my_devices import nxos1_dict, nxos2_dict

env = Environment(undefined = StrictUndefined)
env.loader = FileSystemLoader(".")

as_num = 22
nxos1_temp_dict = {"nxos_int": "Ethernet1/2", "nxos_ip": "10.1.250.1", "nxos_subnet": 24,
                    "nxos_local_as": as_num, "nxos_remote_as": as_num}
nxos2_temp_dict = {"nxos_int": "Ethernet1/2", "nxos_ip": "10.1.250.2", "nxos_subnet": 24,
                    "nxos_local_as": as_num, "nxos_remote_as": as_num}

nxos1_temp_dict["nxos_peer_ip"] = nxos2_temp_dict["nxos_ip"]
nxos2_temp_dict["nxos_peer_ip"] = nxos1_temp_dict["nxos_ip"]

nxos1_t = env.get_template("Ex2b.j2")
nxos1_op = nxos1_t.render(nxos1_temp_dict)
nxos1_op_lines = [line.strip() for line in nxos1_op.splitlines()]
nxos1_connect = ConnectHandler(**nxos1_dict)
nxos1_cmd_op  = nxos1_connect.send_config_set(nxos1_op_lines)
nxos1_connect.disconnect()
print(nxos1_cmd_op)

nxos2_t = env.get_template("Ex2b.j2")
nxos2_op = nxos2_t.render(nxos2_temp_dict)
nxos2_op_lines = [line.strip() for line in nxos2_op.splitlines()]
nxos2_connect = ConnectHandler(**nxos2_dict)
nxos2_cmd_op  = nxos2_connect.send_config_set(nxos2_op_lines)
nxos2_connect.disconnect()
print(nxos2_cmd_op)
