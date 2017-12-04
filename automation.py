#!/usr/bin/env python
import pexpect
import getpass
import time
import switchlist_error
timestr = time.strftime("%Y%m%d-%H%M%S")


for ip_list in switchlist_error.iplist:
  for ip_dict in ip_list:
    try:
        sshcmdx='telnet ' + ip_list[ip_dict] 
		#sshcmdx='ssh -q ' + 'testadmin' + '@' + iplist[ip] 
        p=pexpect.spawn(sshcmdx)
        a=p.expect (['Username:', 'Press'])
        print ("value of a %d",a)
        if a == 0:
          p.sendline('testadmin')
          p.expect('Password:')
          p.sendline(switchlist_error.pw)
          for cmd in switchlist_error.cmdlist:
            p.sendline(cmd)
	  filename=ip_dict + "_" + timestr + ".log"
          filename_out=file(filename,'w')
          p.logfile=filename_out
          p.interact()
        elif a == 1:
          p.sendline()
          p.sendline('testadmin')
          p.expect('Password:')
          p.sendline(switchlist_error.pw)
          for cmd in switchlist_error.cmdlist:
            p.sendline(cmd)
	  filename=ip_dict + "_" + timestr + ".log"
          filename_out=file(filename,'w')
          p.logfile=filename_out
          p.interact()

    except Exception as e:
      filename=ip_dict + "_" + timestr + "_error.log"
      filename_out=file(filename,'w')
      p.logfile=filename_out
      p.interact()

