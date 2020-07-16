from Ex1_devices import device_list
from Ex2_functions import ssh_command
from datetime import datetime
import threading

start_time = datetime.now()

threads = []

for device in device_list:
    t = threading.Thread(target = ssh_command, args = (device, "show version"))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end_time = datetime.now()

print(f"Total time taken to generate the 'show version'output from all the devices: {end_time - start_time}")

