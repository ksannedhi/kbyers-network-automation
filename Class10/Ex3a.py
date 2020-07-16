'''Create a new function that is a duplicate of your "ssh_command" function. Name this function "ssh_command2".
This function should eliminate all printing to standard output and should instead return the show command output.
Note, in general, it is problematic to print in the child thread as you can get into race conditions between the threads.
Using the "ThreadPoolExecutor" in Concurrent Futures execute "show version" on each of the devices defined in my_devices.py.
Use the 'wait' method to ensure all of the futures have completed. Concurrent futures should be executing the ssh_command2 function in the child threads.
Print the total execution time required to accomplish this task.'''

from concurrent.futures import ThreadPoolExecutor, wait
from Ex2_functions import ssh_command2
from Ex1_devices import device_list
from datetime import datetime

start_time = datetime.now()

max_threads = 5
pool = ThreadPoolExecutor(max_threads)
futures = []

for device in device_list:
    futures.append(pool.submit(ssh_command2, device, "show version"))

wait(futures)

for future in futures:
    print(future.result())

end_time = datetime.now()

print(f"Total time taken to execute 'show version' on all the devices: {end_time - start_time}")
