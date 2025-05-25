#!/usr/bin/env python

import getpass
from datetime import datetime
from netmiko import ConnectHandler

# Standard OSPF configuration template
def ospf_template(process_id, area_id, address_family, interface, network):
    return [
        f"router ospf {process_id}",
        f"area {area_id} interface {interface}",
        f"address-family {address_family} unicast",
        f"network {network} area {area_id}"
    ]

# Standard BGP configuration template
def bgp_template(as_number, neighbor_ip, network, address_family):
    return [
        f"router bgp {as_number}",
        f"neighbor {neighbor_ip} remote-as {as_number}",
        f"address-family {address_family}",
        f"network {network}"
    ]

# Function to configure protocol on a Cisco device
def configure_protocol(device_ip, username, password, config_template, protocol_name):
    device = {
        'device_type': 'cisco_xr',
        'host': device_ip,
        'username': username,
        'password': password,
    }
    
    try:
        with ConnectHandler(**device) as ssh:
            print(f"Connected to device with IP: {device_ip}")

            print(f"Configuring {protocol_name} on {device_ip}:")
            protocol_params = {}
            for param in config_template.__code__.co_varnames[1:len(config_template.__code__.co_varnames)]:
                protocol_params[param] = input(f"Enter {param.replace('_', ' ').title()}: ")

            config_commands = config_template(**protocol_params)

            output = ssh.send_config_set(config_commands)
            print(output)

    except Exception as e:
        print(f"An error occurred while configuring {protocol_name} on {device_ip}: {e}")

# Main script
if __name__ == "__main__":
    username = input("Enter username: ")
    password = getpass.getpass("Enter your SSH password: ")
    
    timestamp_start = datetime.now()
    print(f"Script started at: {timestamp_start}")

    devices_count = int(input("How many devices do you want to configure? "))
    
    for _ in range(devices_count):
        device_ip = input("Enter IP address for the device: ")

        ospf_process_id = input("Enter OSPF Process ID: ")
        ospf_area_id = input("Enter OSPF Area ID: ")
        ospf_address_family = input("Enter Address Family for OSPF (ipv4 or ipv6): ")
        ospf_interface = input("Enter Interface for OSPF (e.g., GigabitEthernet0/0/0/0): ")
        ospf_network = input("Enter Network for OSPF (e.g., 192.168.1.0 0.0.0.255): ")

        configure_protocol(device_ip, username, password, ospf_template, "OSPF")

        bgp_as_number = input("Enter BGP AS Number: ")
        bgp_neighbor_ip = input("Enter BGP Neighbor IP: ")
        bgp_network = input("Enter Network to Advertise for BGP: ")
        bgp_address_family = input("Enter Address Family for BGP (ipv4 or ipv6): ")

        configure_protocol(device_ip, username, password, bgp_template, "BGP")
    
    timestamp_end = datetime.now()
    print(f"Script finished at: {timestamp_end}")