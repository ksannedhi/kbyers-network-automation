from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from getpass import getpass

srx1 = Device(host = "srx1.lasthop.io", user = "pyclass", password = getpass())
srx1.open()

cfg = Config(srx1)
cfg.lock()

cfg.load("set system host-name test123", format = "set", merge = True)
print(cfg.diff())

cfg.commit(comment = "Changing the hostname")

cfg.unlock()

