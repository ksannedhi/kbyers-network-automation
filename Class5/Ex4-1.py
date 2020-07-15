'''Expand on exercise3 except use a for-loop to configure five VRFs. Each VRF should have a unique name and a unique route distinguisher.
Each VRF should once again have the IPv4 and the IPv6 address families controlled by a conditional-variable passed into the template.
Note, you will want to pass in a list or dictionary of VRFs that you loop over in your Jinja2 template.'''

from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined = StrictUndefined)
env.loader = FileSystemLoader(".")

vrf_data = [{"vrf_name": "blue", "rd_number": "100.1", "ipv4_enabled": True, "ipv6_enabled": False},
            {"vrf_name": "red", "rd_number": "200.2", "ipv4_enabled": False, "ipv6_enabled": True},
            {"vrf_name": "green", "rd_number": "300.3", "ipv4_enabled": True, "ipv6_enabled": False},
            {"vrf_name": "yellow", "rd_number": "400.4", "ipv4_enabled": False, "ipv6_enabled": True},
            {"vrf_name": "brown", "rd_number": "500.5", "ipv4_enabled": True, "ipv6_enabled": True}]

vrf_vars = {"all_vrfs": vrf_data}

t = env.get_template("Ex4-1.j2")
print(t.render(vrf_vars))
