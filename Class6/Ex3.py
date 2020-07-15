'''Using your external YAML file and your function located in my_funcs.py, use pyeapi to connect to arista4.lasthop.io and retrieve "show ip route".
From this routing table data, extract all of the static and connected routes from the default VRF.
Print these routes to the screen and indicate whether the route is a connected route or a static route.
In the case of a static route, print the next hop address.'''

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
