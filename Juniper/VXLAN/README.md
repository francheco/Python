


### Provisioning


# Install Netmiko

 First, please ensure the 'netmiko' library is installed in your Python environment.

pip3 install netmiko
pip3 show netmiko
pip3 install --upgrade netmiko


# Make your Python script executable

Add Execution Permission

chmod +x YourScript.py

Execute the Script

./YourScript.py

# Please consider you can also schedule your script as I show depict 

##### Schedule your script to run automatically 


Here's how you can schedule your Python script using crontab:


Open a terminal window and type
crontab -e
minute hour * * * /path/to/python /path/to/your/script.py

Please remember when executing crontab that it should open a text editor like Nano or vim, 
make sure you save the changes before applying the script





### Considerations



The code prompts you to input the necessary details and configurations for VLANs, VRF, OSPF, and BGP, which are fundamental to setting up VXLAN EVPN. Here's how the code covers the requirements:

Device Parameters: The script prompts you to enter device-specific details such as IP address, SSH credentials, management IP, and VLAN ID for each device.

VLAN Configuration: You can input the interface, VLAN ID, and IP address required for VLAN setup.

VRF Configuration: Users can specify VRF parameters like name, interface, RD, and RT to segregate and route traffic.

OSPF Configuration: To establish routing relationships between devices, you can define the OSPF area and neighbours.

BGP Configuration: The code allows setting up BGP parameters, including neighbour details and AS numbers, and enables the EVPN address family, which is essential for VXLAN EVPN.

While this script provides a foundational setup for VXLAN EVPN, please ensure your network requirements are fully addressed.
