from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined = StrictUndefined)
env.loader = FileSystemLoader(".")

include_vars = {"ntp_server1": "130.126.24.24", "ntp_server2": "152.2.21.106"}

t = env.get_template("Ex5_base_template.j2")
print(t.render(include_vars))

