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

