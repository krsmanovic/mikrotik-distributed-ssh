# MikroTik SSH script based on Python "paramiko" module

This is a tool for executing many MikroTik commands from external `commands` file to many MikroTik routers listed in `hosts` file. Use this type of script only if you are not able to setup ssh keys for whatever the reason. Remember to remove all credentials left in clear text after you have finished your work!

Log files `error.log` and `success.log` are created since it is very important to know if something went wrong when batch configuring many devices.

## 1) Setup the inventory and commands

Populate the files `hosts` (inventory) and `commands` according to your task. Smaple files are provided in `/scripts` folder together with the source code.

## 2) Enter the credentials within the script

Edit the mt_username and mt_password variables to fit your credentials.

It is strongly advised never to keep credentials in clear text and use ssh keys where possible! Remember to remove credentials after you are finished with your work!

## 3) Run the script

Simply start the script with
```
python mikrotik-ssh.py
```
