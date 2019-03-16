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

# Parsing and using the arguments
args = parser.parse_args()

input_cmd = args.INPUT_CMD
target_dev = args.TARGET_DEV

processes=[]
#timestr = time.strftime("%Y%m%d-%H%M%S")
start_time=datetime.now()
date_time=start_time.strftime("%Y%m%d-%H%M%S")

def connect_dev(ip):
  sshcmdx='ssh -o StrictHostKeyChecking=no ' + 'root@' + ip
  p=testmod.spawn(sshcmdx)
  for cmd in input_cmd:
    p.expect(".")
    p.sendline(cmd)
    filename=ip+"_" + date_time + ".log"
    filename_out=file(filename,'w')
    p.logfile=filename_out
  p.sendline('exit')
  p.interact()

for i in target_dev:
  processes.append(mp.Process(target=connect_dev, args=[i]))

for p in processes:
  p.start()

for p in processes:
  p.join()

end_time=datetime.now()
print("Script Execution time {}".format(end_time-start_time))
