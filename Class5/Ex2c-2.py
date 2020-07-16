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
