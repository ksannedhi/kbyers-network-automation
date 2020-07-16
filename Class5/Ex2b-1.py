'''Expand your Jinja2 template such that both the following interface and BGP configurations are generated for nxos1 and nxos2.
The interface name, IP address, netmask, local_as, and peer_ip should all be variables in the template.
This is iBGP so the remote_as will be the same as the local_as.
nxos1
interface Ethernet1/1
  ip address 10.1.100.1/24
router bgp 22
  neighbor 10.1.100.2 remote-as 22
    address-family ipv4 unicast
nxos2
interface Ethernet1/1
  ip address 10.1.100.2/24
router bgp 22
  neighbor 10.1.100.1 remote-as 22
    address-family ipv4 unicast'''

from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined = StrictUndefined)
env.loader = FileSystemLoader(".")

interface = "Ethernet1/1"
as_num = 22
nxos1_vars = {"intf_name": interface, "ip_addr": "10.1.100.1", "net_mask": 24, "local_as": as_num, "remote_as": as_num}
nxos2_vars = {"intf_name": interface, "ip_addr": "10.1.100.2", "net_mask": 24, "local_as": as_num, "remote_as": as_num}
nxos1_vars["neighbor_ip"] = nxos2_vars["ip_addr"]
nxos2_vars["neighbor_ip"] = nxos1_vars["ip_addr"]

for nxos_vars in (nxos1_vars, nxos2_vars):
    t = env.get_template("Ex2b-1.j2")
    print(t.render(nxos_vars))
