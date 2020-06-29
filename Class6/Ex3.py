from Ex2b_my_funcs import yaml_load
from getpass import getpass
import pyeapi

devices = yaml_load()
arista4_dict = devices["arista4"]
arista4_dict["password"] = getpass()

connection = pyeapi.client.connect(**arista4_dict)
device = pyeapi.client.Node(connection)
output = device.enable("show ip route")
routes = output[0]["result"]["vrfs"]["default"]["routes"]

for network, route_params in routes.items():
    if route_params["routeType"] == "static":
        print(f"Route to network {network} is static and it's next hop IP address is {route_params['vias'][0]['nexthopAddr']}")
    else:
        print(f'Route to network {network} is directly connected.')
