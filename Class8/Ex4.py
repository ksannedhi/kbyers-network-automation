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
