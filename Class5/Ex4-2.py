from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined = StrictUndefined)
env.loader = FileSystemLoader(".")

vrf_list = [{"Blue": {"vrf_name": "blue", "rd_number": "100.1", "ipv4_enabled": True, "ipv6_enabled": True}},
            {"Red": {"vrf_name": "red", "rd_number": "200.1", "ipv4_enabled": False, "ipv6_enabled": True}},
            {"Green": {"vrf_name": "green", "rd_number": "300.1", "ipv4_enabled": True, "ipv6_enabled": False}},
            {"Brown": {"vrf_name": "brown", "rd_number": "400.1", "ipv4_enabled": False, "ipv6_enabled": True}},
            {"Yellow": {"vrf_name": "yellow", "rd_number": "500.1", "ipv4_enabled": True, "ipv6_enabled": False}}]

for vrf in vrf_list:
    for vrf_name,vrf_details in vrf.items():
        vrf_vars = vrf_details
        t= env.get_template("Ex3-1.j2")
        print(t.render(vrf_vars))

