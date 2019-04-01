# Remote Automation

Automatically connect to multiple remote device, execute multiple commands and each device output will be saved to a file in the specified directory that contains the name of the device and time when the script is executed. At the end of the output of each script will show the length of time it take to run the script. In general, this script can be used on client server devices and also networking devices.

The auto_command.py does not utilize multiprocess where as auto_command_mp.py utilizes multiprocess which renders it to complete about twice faster based on test results.

# Getting Started

The script excepts three types of arguments which are grouped as --INPUT_CMD which is list of target commands to be executed at the target remote device, --TARGET_DEV which is list of target devices where the commands to be performed, --TARGET_DIR which is the target directory where the output file to be created.

# Example

./auto_command.py --INPUT_CMD 'date' 'ls -las' 'time nslookup "www.google.com"' --TARGET_DEV '192.168.1.1' '192.168.1.2' --TARGET_DIR '/output/'
