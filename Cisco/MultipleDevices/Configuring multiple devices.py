#!/usr/bin/env python


from netmiko import ConnectHandler
import getpass
import datetime

# Function to configure a device using provided configuration
def configure_device(device, configuration):
    # Read configuration commands from the provided file
    with open(configuration, 'r') as file:
        config_commands = file.read().splitlines()

    # Connect to the device
    conn = ConnectHandler(**device)

    # Send configuration commands to the device
    conn.send_config_set(config_commands)

    # Disconnect from the device after configuration
    conn.disconnect()

# List of devices to configure - each device has its own configuration file
devices = [
    {
        'device_type': 'cisco_xe',
        'host': 'switch1_ip',
        'username': 'your_username',
        'password': '',  # We will prompt for this
        'config_file': 'config_switch1.txt'
    },
    {
        'device_type': 'cisco_xe',
        'host': 'switch2_ip',
        'username': 'your_username',
        'password': '',  # We will prompt for this
        'config_file': 'config_switch2.txt'
    },
    {
        'device_type': 'cisco_xe',
        'host': 'switch3_ip',
        'username': 'your_username',
        'password': '',  # We will prompt for this
        'config_file': 'config_switch3.txt'
    }
]

# Prompt for the SSH password securely
password = getpass.getpass("Enter your SSH password: ")

start_time = datetime.datetime.now()

# Loop through each device, update the password, and configure with respective configuration file
for device in devices:
    device['password'] = password
    configure_device(device, device['config_file'])

end_time = datetime.datetime.now()
total_time = end_time - start_time

# Display the script execution start and end time along with total time taken
print(f"Script started at: {start_time}")
print(f"Script finished at: {end_time}")
print(f"Total time taken: {total_time}")