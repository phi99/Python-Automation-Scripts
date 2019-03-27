import argparse
import testmod
import multiprocessing as mp
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

#convert target directory to string
str_target_dir=''.join(str(e) for e in target_dir)

processes=[]

#Get start time
start_time=datetime.now()
date_time=start_time.strftime("%Y%m%d-%H%M%S")

#Function to connect to device, run cmd, and save output file
def connect_dev(ip,input_cmd,str_target_dir):
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

#Spawn new process for each device
for i in target_dev:
  processes.append(mp.Process(target=connect_dev, args=[i,input_cmd,str_target_dir]))

for a in processes:
  a.start()

for a in processes:
  a.join()

#Get end time
end_time=datetime.now()

#Get time it takes to run the script
print("Script Execution time {}".format(end_time-start_time))
