'''Use Python and Jinja2 to generate the below NX-OS interface configuration. You should use an external template file and a Jinja2 environment to accomplish this.
The interface, ip_address, and netmask should all be variables in the Jinja2 template.
 
nxos1
interface Ethernet1/1
  ip address 10.1.100.1/24
nxos2
interface Ethernet1/1
  ip address 10.1.100.2/24'''

from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined = StrictUndefined)
env.loader = FileSystemLoader(".")

interface = "Ethernet1/1"
nxos1_vars = {"intf_name": interface, "ip_addr": "10.1.100.1", "net_mask": 24}
nxos2_vars = {"intf_name": interface, "ip_addr": "10.1.100.2", "net_mask": 24}

for nxos_vars in (nxos1_vars, nxos2_vars):
    t = env.get_template("Ex2a-1.j2")
    print(t.render(nxos_vars))
