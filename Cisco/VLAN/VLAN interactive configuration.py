#!/usr/bin/env python


import getpass
from datetime import datetime
from netmiko import ConnectHandler

# Function: Configure VLAN on a Cisco IOS device
def configure_vlan(device_ip, username, password):
    # Define device parameters for Netmiko connection
    device = {
        'device_type': 'cisco_ios',
        'host': device_ip,
        'username': username,
        'password': password,
    }
    
    # Connect to the device
    net_connect = ConnectHandler(**device)
    
    # Display start message for the device configuration
    print(f"Start configuring device with IP: {device_ip}")
    
    # Collect VLAN information from the user
    vlan_id = input("Enter VLAN ID: ")
    print(f"Configuring VLAN {vlan_id} on device with IP: {device_ip}")
    vlan_name = input("Enter VLAN Name: ")
    vlan_mode = input("Enter VLAN Mode (Access or Trunk): ")
    ports_assignment = input("Enter Ports Assignment: ")
    
    # Define configuration commands for the VLAN
    config_commands = [
        f"vlan {vlan_id}",
        f"name {vlan_name}",
        f"interface {ports_assignment}",
        f"switchport mode {vlan_mode}"
    ]
    
    # Send configuration commands to the device
    output = net_connect.send_config_set(config_commands)
    print(output)
    
    # Disconnect from the device after configuring the VLAN
    net_connect.disconnect()
    
    # Display completion message for the VLAN configuration
    print(f"Configuration for VLAN {vlan_id} on device with IP {device_ip} completed")

# Function: Log timestamp
def log_timestamp(message):
    # Create a timestamp with the current date and time
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Print the timestamp along with a custom message
    print(f"{timestamp} - {message}")

if __name__ == "__main__":
    # Log the start of the script
    log_timestamp("Script started")
    
    # Prompt the user for their username and password
    username = input("Enter username: ")
    password = getpass.getpass("Enter your SSH password: ")
    
    # Prompt for the number of devices to configure
    devices_count = int(input("How many devices do you want to configure VLANs on? "))
    
    # Configure VLANs on each device based on user input
    for _ in range(devices_count):
        device_ip = input("Enter Cisco IOS device IP: ")
        configure_vlan(device_ip, username, password)
    
    # Log the completion of the script
    log_timestamp("Script finished")