# -----------------------------------------------------------
# Creating a website blocker using python.
#
# (C) 2020 Sandra VS Nair, Trivandrum
# email sandravsnair@gmail.com
# -----------------------------------------------------------

import time
from datetime import timedelta as td
from datetime import datetime as dt 

#Specify the path of hosts file.
host_path=r"C:\Windows\System32\drivers\etc\hosts"

#Specify the list of websites you want to block.
website_list=["www.facebook.com","facebook.com","www.gmail.com","gmail.com"]
local_host = "127.0.0.1"

#Considering working hours as 9-4.
#This portion of code runs continuously.
while True:
    #If the current time is in between the working hours,the websites to be blocked are redirected into 127.0.0.1. 
    #Then, the program sleeps till the working hour ends.

    if dt(dt.now().year,dt.now().month,dt.now().day,9) <  dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        with open(host_path,"a") as file:
            for website in website_list:
                file.write(local_host+" "+website+"\n")
        time_left=dt(dt.now().year,dt.now().month,dt.now().day,16)-dt.now()
        time.sleep(time_left.total_seconds())

    #If the current time is not in between the working hours, the websites are unblocked.
    #Then the program sleeps till the next working hour starts.      
    else:
        with open(host_path,"r+") as file:
            lines=file.readlines()
            file.seek(0)
            for line in lines:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        if dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,9):     
            next_work_hour = dt(dt.now().year,dt.now().month,dt.now().day,9)
        else:
            next_work_hour = dt(dt.now().year,dt.now().month,dt.now().day,9) + td(days=1)
        time_left=next_work_hour-dt.now()
        time.sleep(time_left.total_seconds())         
     

        