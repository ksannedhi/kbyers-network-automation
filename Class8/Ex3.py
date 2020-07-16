"""3a. Open a connection to the srx2 device and acquire a configuration lock.
Validate that the configuration session is indeed locked by SSH'ing into the device and attempting to enter configuration mode ("configure").
Reuse, the 'srx2' device definition from the jnpr_devices.py file that you created in exercise2.

You should receive a prompt similar to the following:
pyclass@srx2> configure
Entering configuration mode
Users currently editing the configuration:
  pyclass (pid 30316) on since 2019-03-08 18:30:51 PST
      exclusive

Add code to attempt to lock the configuration again. Gracefully handle the "LockError" exception (meaning the configuration is already locked).

3b. Use the "load" method to stage a configuration using a basic set command, for example, "set system host-name python4life".

3c. Print the diff of the current configuration with the staged configuration. Your output should look similar to the following:
[edit system]
-  host-name srx2;
+  host-name python4life;

3d. Rollback the staged configuration. Once again, print out the diff of the staged and the current configuration (which at this point should be None)."""

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
