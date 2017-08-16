## MikroTik SSH script written in Python (based on "paramiko" module)

This is a tool for executing many MikroTik commands from external file to many MikroTik routers listed in `hosts` file. Log file is also created, since it is very important to know if something went wrong when batch configuring many devices.

Run the script by issuing
```
python mikrotik_ssh.py
```

Example files are included in `/script` folder together with Python source.
