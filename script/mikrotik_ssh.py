#!usr/bin/python

import socket
import errno
import sys
import time
try:
    import paramiko
except ImportError:
    sys.tracebacklimit=0
    print "\r"
    with open("error.log","ab") as e:
        e.write(time.strftime("%Y.%m.%d") + " " + time.strftime("%H:%M:%S") + " \"Paramiko\" module missing! Please visit http://www.paramiko.org/installing.html for more details." + "\r\n")
    e.close()
    raise ImportError("Please install \"paramiko\" module! Visit http://www.paramiko.org/installing.html for more details.\r\n")

nlines = 0
f = open("hosts","r")
mt_username = "admin_username"
mt_password = "admin_password"
timeout = 10
wrong_login = "Access denied"

for line in f:
    
    if nlines > 0:
        print "\r\nWaiting 3s before logging on to the next device...\n"
        time.sleep(3)
    
    nlines += 1
    conn_date = time.strftime("%Y.%m.%d")
    conn_time = time.strftime("%H:%M:%S")
    host = line.rstrip("\n")
    ssh = paramiko.SSHClient()
    
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    print "\r\nConnecting to " + str(nlines) + ". host: " + host + "\r\n"

    try: 
        ssh.connect(host,username=mt_username,password=mt_password,timeout=timeout)

    except socket.timeout as e:
        print "\r\nConnection timeout. Log entry created."
        with open("error.log","ab") as e:
            e.write(conn_date + " " + conn_time + " " + mt_username + "@" + host + " Timeout connecting to the device." + "\r\n")
        e.close()
        continue

    except paramiko.AuthenticationException:
        print "\r\nWrong credentials. Log entry created."
        with open("error.log","ab") as e:
            e.write(conn_date + " " + conn_time + " " + mt_username + "@" + host + " Wrong credentials." + "\r\n")
        e.close()
        continue

    except:
        print "\r\nError connecting to the device. Log entry created."
        with open("error.log","ab") as e:
            e.write(conn_date + " " + conn_time + " "  + mt_username + "@" + host + " Unknown error while connecting to the device." + "\r\n")
        e.close()
        continue

    print "\r\nSuccsessfully connected to the host. Executing commands from the external file:\r\n"
    
    k = open("commands","r")
    for line in k:
        mt_command = line.rstrip("\n")
        time.sleep(.3)
        stdin, stdout, stderr = ssh.exec_command(mt_command)
        print mt_command

    print "\nExternal commands are executed successfully.\n"
    k.close()
    ssh.get_transport().close()
    ssh.close()
        
print "\nEnd of the program.\n"
f.close()
quit()
