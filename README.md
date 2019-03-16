# Remote Automation
Connect to multiple remote device, execute multiple commands and each device output will be saved to a file that contains the name of the device and time when the script is executed. At the end of the output of each script will show the length of time it take to run the script. In general, this script can be used on client server devices and also networking devices.

# Getting Started
The script excepts two type of arguments which are grouped as --INPUT_CMD which are list of commands wants to be executed at the target remote device and --TARGET_DEV which are list of target devices where the commands to be performed

# Example
./auto_connect.py --INPUT_CMD 'date' 'cat /click/big_acl/acl_list_xml' 'time nslookup "www.google.com"' --TARGET_DEV '192.168.1.1' '192.168.1.2'




