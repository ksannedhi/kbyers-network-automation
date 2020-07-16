from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import LockError
from jnpr_devices import srx1

srx1 = Device(**srx1)
srx1.open()

cfg = Config(srx1)
cfg.lock()

try:
    cfg.lock()
    print("Lock successfully acquired!")
except LockError:
    print("Device was already locked!")

cfg.load("set system host-name srx1-1", format = "set", merge = True)
print(cfg.diff())

cfg.rollback(0)
print(cfg.diff())

