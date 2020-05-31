# Creating a website blocker using Python.

This project demonstrates creation of a website blocker using Python. The websites specified in a list will be blocked during working hours. In this code, the working hours are considered to be from 9 to 4. If the current time is in between the working hours, the websites to be blocked are redirected to 127.0.0.1 and the program sleeps till working hours ends. Else, the websites are unblocked and the programs will sleep till working hours start.

## Prerequisites
Since we are editing the hosts file which need administrative access, you will have to run the program as administrator. This program is written for Windows Operating System. With minimal changes, it can be used for Linux and Mac as well. But both will need sudo access to run the file.

## Usage

1. Run the python file website-blocker.py. Use the commands below in any terminal.
```
python website-blocker.py

```
or if the python version is 3, use command.

```
python3 website-blocker.py

```
or you can also use any python IDE.

You can also use task scheduler and convert the .py file into .pyw to schedule the running of program in background (in Windows). In Linux, you probably have to use crontab to schedule running of program.