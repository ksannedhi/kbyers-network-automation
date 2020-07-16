'''4a. Using the previously created jnpr_devices.py file, open a connection to srx2 and gather the current routing table information.

4b. Using PyEZ stage a configuration from a file. The file should be "conf" notation. This configuration should add two static host routes (routed to discard).
These routes should be from the RFC documentation range of 203.0.113.0/24 (picking any /32 in that range should be fine). Use "merge=True" for this configuration. For example:
routing-options {
    static {
        route 203.0.113.5/32 discard;
        route 203.0.113.200/32 discard;
    }
}

4c. Reusing your gather_routes() function from exercise2, retrieve the routing table before and after you configuration change.
Print out the differences in the routing table (before and after the change).
To simplify the problem, you can assume that the only change will be *additional* routes added by your script.

4d. Using PyEZ delete the static routes that you just added. You can use either load() and set operations or load() plus a configuration file to accomplish this.'''

from jnpr_devices import srx1
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.op.routes import RouteTable

srx1 = Device(**srx1)
srx1.open()

routes = RouteTable(srx1)
routes.get()

print("Routing table before any changes:")
print("=" * 33)
print(routes.items())

cfg = Config(srx1)
cfg.lock()

cfg.load(path = "Ex4.conf", format = "text", merge = True)
print(cfg.diff())

cfg.commit()
cfg.unlock()

routes = RouteTable(srx1)
routes.get()

print("New routes:")
print("=" * 11)
print(routes.items())

cfg.lock()
cfg.load("delete routing-options static route 203.0.113.5/32", format = "set", merge = True)
cfg.load("delete routing-options static route 203.0.113.200/32", format = "set", merge = True)

print(cfg.diff())
cfg.commit()
cfg.unlock()

routes = RouteTable(srx1)
routes.get()

print("Routes after discarding the latest changes:")
print("=" * 43)
print(routes.items())
