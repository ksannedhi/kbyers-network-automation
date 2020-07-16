from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from getpass import getpass

srx2 = Device(host = "srx2.lasthop.io", user = "pyclass", password = getpass())
srx2.open()

cfg = Config(srx2)
cfg.lock()

cfg.load(path = "set_config.conf", format = "set", merge = True)
print(cfg.diff())
cfg.commit(comment = "Changing hostname via external text file.")
cfg.unlock()

