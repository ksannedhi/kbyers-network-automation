from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined = StrictUndefined)
env.loader = FileSystemLoader(".")

vrf_data_dict = {"vrf1": ["blue", "100:1", True, False],
            "vrf2": ["red", "200:2", False, True],
            "vrf3": ["green", "300:3", True, False],
            "vrf4": ["yellow", "400:4", False, True],
            "vrf5": ["brown", "500:5", True, True]}
vrf_vars = {"vrf_data": vrf_data_dict}

t = env.get_template("Ex4.j2")
print(t.render(vrf_vars))

