import argparse
import testmod
from datetime import datetime

__authors__=["the dude"]
__date__='March 2019'
__description__ = 'Simple auto connect script'

parser=argparse.ArgumentParser(
    description=__description__,
    epilog="Created on {}".format(__date__)
)

# Add Positional Arguments
parser.add_argument("--INPUT_CMD",nargs='+',default=[], help="Command to be executed")
parser.add_argument("--TARGET_DEV",nargs='+',default=[],help="Target Device to login to")
parser.add_argument("--TARGET_DIR",nargs='+',default=[],help="Target Directory of output file")


# Parsing and using the arguments
args = parser.parse_args()

input_cmd = args.INPUT_CMD
target_dev = args.TARGET_DEV
target_dir = args.TARGET_DIR
str_target_dir=''.join(str(e) for e in target_dir)

#Get start time
start_time=datetime.now()
date_time=start_time.strftime("%Y%m%d-%H%M%S")

#Execute the commands in devices
for ip in target_dev:
  sshcmdx='ssh -o StrictHostKeyChecking=no ' + 'root@' + ip
  p=testmod.spawn(sshcmdx)
  for cmd in input_cmd:
    p.expect(".")
    p.sendline(cmd)
    filename=str_target_dir+ip+"_" + date_time + ".log"
    filename_out=file(filename,'w')
    p.logfile=filename_out
  p.sendline('exit')
  p.interact()

#Get the end time
end_time=datetime.now()

#Obtain time it takes to run the script
print("Script Execution time {}".format(end_time-start_time))
