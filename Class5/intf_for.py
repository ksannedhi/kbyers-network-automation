from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined = StrictUndefined)
env.loader = FileSystemLoader(".")

intf_list = []
for num in range(24):
    intf = "GigabitInterface1/0/" + str(num)
    intf_list.append(intf)

intf_dict = {"all_ints": intf_list}

t = env.get_template("intf_temp.j2")
print(t.render(intf_dict))
