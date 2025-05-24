### Import modules

import time     # To pauses
import re       # To regex
import os
import io
import ipaddress  # Module for work with IP address range
import platform     # To check OS type
import subprocess   # To run OS commands, such "ping"
import getpass      # To input password in safe mode
import concurrent.futures # This is the module that will give us the ability to setup multi-threading.
#import textfsm      # To parse output of equipments
from pprint import pprint   # To usable print output
#from tabulate import tabulate    # To usable table output
#import xlsxwriter   # To save the files in Excel format
from netmiko import ConnectHandler      # To work with network equipment
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed   # Parallel work some processes


# Devices where we want to get the show commands

DS01_hostname= "DS01-07-HQ01-MX"
DS02_hostname= "DS02-07-HQ01-MX"
SW01_hostname= "SW01-07-HQ01-MX"


# Describing device type, IP address, username and password in plain text haha for authentication


DS01 = { 
'device_type': 'cisco_xe',
'host': 'x.x.x.x',
'username': 'your_username',
"password": "your_password", 
}

DS02 = { 
'device_type': 'cisco_xe',
'host': '172.24.247.222',
'username': 'your_username',
"password": "your_password", 
}

SW01 = { 
'device_type': 'cisco_xe',
'host': '172.24.72.1',
'username': 'your_username',
"password": "your_password",
}

#all_devices = [SW01,DS01,DS02,]

"""for device in all_devices:
    #net_connect = ConnectHandler(device_type=device['device_type'], ip=device['host'], username=device['username'], password=device['password'])
    Tstart = datetime.now()
    print("\n")
    print(Tstart)
   """ 

# Connecting to each device to run the show commands from the .txt file and saving it on a directory in your local machine

net_connect1 = ConnectHandler(**DS01)

with open ("/your_path.txt","r+") as x:                 # open it the .txt file from the directory
    Tstart = datetime.now()
    print("\n")
    print(Tstart)
    print("Starting running show commands on this device",DS01_hostname)
    print("\n Loading configuration..........")
    x=net_connect1.send_config_from_file("show_commands.txt")
    
with open ("/your_path.txt","w+") as f:
    f.write(x)
    print("\n")
    print("Ending running show commands on this device this device", DS01_hostname)
    print("\n ....Configuration loaded")

    print("\n")    
    Tend = datetime.now()
    Tdiff = Tend - Tstart
    print("Time taken to push the configuration = " + str(Tdiff))


net_connect2 = ConnectHandler(**DS02)

with open ("/your_path.txt","r+") as x:             # open it the .txt file from the directory
    Tstart = datetime.now()
    print("\n")
    print(Tstart)
    print("Starting running show commands on this device",DS02_hostname)
    print("\n Loading configuration..........")
    x=net_connect2.send_config_from_file("show_commands.txt")
    
with open ("/your_path.txt","w+") as y:
    y.write(x)
    print("\n")
    print("Ending running show commands on this device this device", DS02_hostname)
    print("\n ....Configuration loaded")

    print("\n")    
    Tend = datetime.now()
    Tdiff = Tend - Tstart
    print("Time taken to push the configuration = " + str(Tdiff))


net_connect3 = ConnectHandler(**SW01)

with open ("/your_path.txt","r+") as x:               # open it the .txt file from the directory
    Tstart = datetime.now()
    print("\n")
    print(Tstart)
    print("Starting running show commands on this device",SW01_hostname)
    print("\n Loading configuration..........")
    x=net_connect3.send_config_from_file("show_commands.txt")
    
with open ("/your_path.txt","w+") as z:
    z.write(x)
    print("\n")
    print("Ending running show commands on this device this device", SW01_hostname)
    print("\n ....Configuration loaded")

    print("\n")    
    Tend = datetime.now()
    Tdiff = Tend - Tstart
    print("Time taken to push the configuration = " + str(Tdiff))