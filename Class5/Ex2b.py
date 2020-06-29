from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined = StrictUndefined)
env.loader = FileSystemLoader(".")

as_num = 22
nxos1_vars = {"nxos_int": "Ethernet1/1", "nxos_ip": "10.1.100.1", "nxos_subnet": 24,
            "nxos_local_as": as_num, "nxos_peer_ip": "10.1.100.2", "nxos_remote_as": as_num}
nxos2_vars = {"nxos_int": "Ethernet1/1", "nxos_ip": "10.1.100.2", "nxos_subnet": 24,
            "nxos_local_as": as_num, "nxos_peer_ip": "10.1.100.1", "nxos_remote_as": as_num}

for nxos_vars in (nxos1_vars, nxos2_vars):
    t = env.get_template("Ex2b.j2")
    print(t.render(nxos_vars))
