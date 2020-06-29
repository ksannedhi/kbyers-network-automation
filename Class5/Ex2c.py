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

