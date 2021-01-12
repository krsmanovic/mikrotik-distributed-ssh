#!usr/bin/python

import socket
import errno
import sys
import time

def time_stamp():
    t = time.strftime("%Y-%m-%d %H:%M:%S")
    return t

try:
    import paramiko
    
except ImportError:
    sys.tracebacklimit=0
    with open("error.log","a") as e:
        e.write(time_stamp() + " \"Paramiko\" module missing! Please visit http://www.paramiko.org/installing.html for more details.\n")
    e.close()
    raise ImportError("\rPlease install \"paramiko\" module! Visit http://www.paramiko.org/installing.html for more details.\r\n")

try:
    f = open("hosts","r")
except IOError:
    sys.tracebacklimit=0
    print("\nFile \"hosts\" does not exist or is not accessible.\n")
    quit()

nlines = 0
mt_username = "script_user"
ssh_key = paramiko.RSAKey.from_private_key_file("key.ppk")
# Using ssh keys is strongly advised!
# If you are unable to setup that method of connecting to your devices, you have the option of the clear text login as well.
# mt_password = "script_password"
timeout = 10

for line in f:

    try:
        k = open("commands","r")
    except IOError:
        sys.tracebacklimit=0
        print("\nFile \"commands\" does not exist or is not accessible.\n")
        quit()
    
    nlines += 1
    host = line.rstrip("\n")
    ssh = paramiko.SSHClient()
    
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    print("\r\n########################################## Connecting to " + str(nlines) + ". host: " + host + " ##########################################\r\n")

    try: 
        ssh.connect(host,username=mt_username,pkey=ssh_key,timeout=timeout)
        # Using ssh keys is strongly advised!
        # ssh.connect(host,username=mt_username,password=mt_password,timeout=timeout)
        
    except socket.timeout as e:
        print("Connection timeout. Log entry created.")
        with open("error.log","a") as e:
            e.write(time_stamp() + " " + host + " Timeout connecting to the device.\n")
        e.close()
        continue

    except paramiko.AuthenticationException:
        print("Wrong credentials. Log entry created.")
        with open("error.log","a") as e:
            e.write(time_stamp() + " " + host + " Wrong credentials.\n")
        e.close()
        continue

    except:
        print("Error connecting to the device. Log entry created.")
        with open("error.log","a") as e:
            e.write(time_stamp() + " " + host + " Unknown error while connecting to the device.\n")
        e.close()
        continue

    print("Succsessfully connected to the host. Executing commands from the external file:\r\n")

    for line in k:
        mt_command = line.rstrip("\n")
        # Adding 200ms delay between commands
        time.sleep(.2)
        stdin, stdout, stderr = ssh.exec_command(mt_command)
        print(mt_command)

    print("\nExternal commands are executed successfully.")
    with open("success.log","a") as s:
        s.write(time_stamp() + " " + host + " Successfully executed commands on the host.\n")
    s.close()
    k.close()
    ssh.get_transport().close()
    ssh.close()
        
if nlines == 0:
    print("\nList of hosts is empty.\n")
else:
    print()
f.close()
quit()
