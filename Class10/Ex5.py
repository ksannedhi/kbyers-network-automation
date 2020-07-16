from concurrent.futures import ProcessPoolExecutor, as_completed
from Ex1_devices import device_list
from Ex2_functions import ssh_command2
from datetime import datetime

start_time = datetime.now()
max_procs = 5

with ProcessPoolExecutor(max_procs) as pool:
    futures = []
    
    for device in device_list:
        futures.append(pool.submit(ssh_command2, device, "show version"))

    for future in as_completed(futures):
        print(future.result())

    end_time = datetime.now()

    print(f"Total time taken to execute 'show version' on all the devices: {end_time - start_time}")

