from Ex1_devices import nxos1_dict
from Ex2_functions import open_napalm_connection, create_checkpoint

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

device = open_napalm_connection(nxos1_dict)
#create_checkpoint(device)

conf_replacement_file = "Ex4_replacement_cfg"

device.load_replace_candidate(filename = "Ex4_replacement_cfg") #Alternately, device.load_replace_candidate(conf_replacement_file)
print("Following changes will take effect after the configuration replacement:")
print(device.compare_config())

print()
input("Hit 'Enter' to continue.")
#print("Discarding changes for now.")
#device.discard_config()
device.commit_config()
print("Changes that will apply:")
print(device.compare_config())

