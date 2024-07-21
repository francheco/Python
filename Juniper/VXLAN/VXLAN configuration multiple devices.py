from netmiko import ConnectHandler
import getpass

# Function to prompt user for device details
def get_device_details(device_num):
    print(f"Configuring Device {device_num}")
    device_ip = input(f"Enter the management IP address of Device {device_num}: ")
    device_username = input(f"Enter the SSH username of Device {device_num}: ")
    device_password = getpass.getpass(f"Enter the SSH password of Device {device_num}: ")
    oob_ip = input(f"Enter the Out-of-Band Management IP address of Device {device_num}: ")
    management_vlan = input(f"Enter the Management VLAN ID of Device {device_num}: ")

    return {
        'device_ip': device_ip,
        'device_username': device_username,
        'device_password': device_password,
        'oob_ip': oob_ip,
        'management_vlan': management_vlan,
        # Add more device-specific parameters as needed
    }

# Main function to configure devices
def configure_devices(num_devices):
    for i in range(1, num_devices + 1):
        device_details = get_device_details(i)

        # Prompt user for VLAN configuration parameters
        print("\n--- Configure VLAN ---")
        interface = input("Enter the interface to configure (e.g., ge-0/0/1): ")
        vlan_id = input("Enter the VLAN ID for the interface: ")
        ip_address = input("Enter the IP address for the interface: ")

        vlan_commands = [
            f'set interfaces {interface} vlan-tagging',
            f'set interfaces {interface} unit 0 vlan-id {vlan_id} family inet address {ip_address}',
        ]

        # Prompt user for VRF configuration parameters
        print("\n--- Configure VRF ---")
        vrf_name = input("Enter the VRF name: ")
        vrf_interface = input("Enter the interface for the VRF (e.g., ge-0/0/1.0): ")
        vrf_rd = input("Enter the Route Distinguisher (RD) for the VRF: ")
        vrf_rt = input("Enter the Route Target (RT) for the VRF: ")

        vrf_commands = [
            f'set routing-instances {vrf_name} instance-type virtual-router',
            f'set routing-instances {vrf_name} interface {vrf_interface}',
            f'set routing-instances {vrf_name} route-distinguisher {vrf_rd}',
            f'set routing-instances {vrf_name} vrf-target target:{vrf_rt}',
        ]

        # Prompt user for OSPF configuration parameters
        print("\n--- Configure OSPF ---")
        ospf_area = input("Enter the OSPF area: ")
        num_neighborships = int(input("Enter the number of OSPF neighborships to create: "))

        ospf_commands = [f'edit protocols ospf area {ospf_area}']

        for n in range(num_neighborships):
            neighbor_ip = input(f"Enter the IP address of OSPF neighbor {n+1}: ")
            ospf_commands.append(f'set protocols ospf neighbor {neighbor_ip}')

        # Prompt user for BGP configuration parameters
        print("\n--- Configure BGP ---")
        bgp_group_name = input("Enter the BGP group name: ")
        bgp_neighbor_ip = input("Enter the IP address of the BGP neighbor: ")
        bgp_peer_as = input("Enter the AS number of the BGP neighbor: ")

        bgp_commands = [
            f'edit protocols bgp group {bgp_group_name} neighbor {bgp_neighbor_ip} peer-as {bgp_peer_as}',
            f'set protocols bgp group {bgp_group_name} family evpn unicast',
            # Add more BGP configurations as needed for EVPN setup
        ]

        try:
            connection = ConnectHandler(**device_details)
            print(f"Connected to {device_details['device_ip']}")

            output_vlan = connection.send_config_set(vlan_commands)
            print(output_vlan)

            output_vrf = connection.send_config_set(vrf_commands)
            print(output_vrf)

            output_ospf = connection.send_config_set(ospf_commands)
            print(output_ospf)

            output_bgp = connection.send_config_set(bgp_commands)
            print(output_bgp)

            connection.disconnect()
            print(f"Disconnected from {device_details['device_ip']}")

        except Exception as e:
            print(f"Failed to connect to {device_details['device_ip']} - {str(e)}")

# Prompt user for the number of devices to configure
num_devices = int(input("Enter the number of devices you want to configure: "))

# Start configuring devices
configure_devices(num_devices)