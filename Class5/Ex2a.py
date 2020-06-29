from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined = StrictUndefined)
env.loader = FileSystemLoader(".")

nxos1_vars = {"nxos1_int": "Ethernet1/1", "nxos1_ip": "10.1.100.1", "nxos1_subnet": 24}
nxos2_vars = {"nxos2_int": "Ethernet1/1", "nxos2_ip": "10.1.100.2", "nxos2_subnet": 24}
nxos_vars = {**nxos1_vars, **nxos2_vars}

t = env.get_template("Ex2a.j2")
print(t.render(nxos_vars))
