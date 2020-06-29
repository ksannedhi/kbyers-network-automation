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

