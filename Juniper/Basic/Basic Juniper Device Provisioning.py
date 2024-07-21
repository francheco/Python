from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.utils.scp import SCP
from jnpr.junos.utils.sw import SW
import getpass


# Prompt user to enter the password
password = getpass.getpass("Enter your password for the Juniper switch: ")

# Connect to the device using SSH
dev = Device(host="switch_ip", user="username", password=password)
dev.open()

# Start the configuration session
with Config(dev, mode='private') as cu:
    ##### User and Password Authentication #####
    # Set the encrypted root password
    cu.load("set system root-authentication encrypted-password <encrypted_password>", format="set")

    ##### IP Management #####
    # Configure management IP address
    cu.load("set interfaces lo0 unit 0 family inet address <ip_address>/32", format="set")

    ##### Basic Interface Addressing #####
    # Configure interfaces with IP addresses
    cu.load("set interfaces ge-0/0/<port_number> unit 0 family inet address <ip_address>/<subnet_mask>", format="set")

    ##### SNMP Configuration #####
    # Configure SNMP community string
    cu.load("set snmp community <community_string> authorization read-only", format="set")

    ##### SSH Connection #####
    # Enable SSH
    cu.load("set system services ssh", format="set")

    ##### Basic VLANs Configuration #####
    # Create VLANs
    cu.load("set vlans vlan-id vlan_id l3-interface irb.<vlan_id>", format="set")

    ##### Out-of-Band Management #####
    # Configure out-of-band management interface
    cu.load("set interfaces me0 unit 0 family inet address <outband_ip_address>/<subnet_mask>", format="set")

    # Commit the changes
    cu.commit()

# Close the connection
dev.close()
