from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined = StrictUndefined)
env.loader = FileSystemLoader(".")

vrf_vars = {"vrf_name": "blue", "rd_number": "100:1", "ipv4_enabled": True, "ipv6_enabled": True}

t = env.get_template("Ex3-1.j2")
print(t.render(vrf_vars))

