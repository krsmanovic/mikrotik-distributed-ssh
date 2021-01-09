# MikroTik SSH script based on Python "paramiko" module

This is a tool for executing many MikroTik commands from external `commands` file to many MikroTik routers listed in `hosts` file. Using ssh keys method is strongly advised! Remember to remove all credentials left in clear text if you opt in for that type of connection!

Log files `error.log` or `success.log` are appended depending on the result of the script execution.

## 1) Setup the inventory and commands

Populate the files `hosts` (inventory) and `commands` according to your task. Sample files are provided in `/scripts` folder together with the source code.

## 2) Enter the credentials within the script

Edit the `mt_username` and `ssh_key` variables according to your environment.

It is strongly advised never to keep credentials in clear text and use ssh keys whenever possible! If you opted in for using clear text passowrd with `mt_password` variable, remember to remove it after you are finished with your work!

## 3) Run the script

Start the script with
```
python mikrotik-ssh.py
```
