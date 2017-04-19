#!/usr/bin/env python3
import os
import subprocess
import emailgen


#
# Header information
#
recipient = input("recipient: ")
sender = input("sender: ")
password = input("sender password: ")
subject = "TeamIT Alert HDD Temp: " + os.uname().nodename

#
# Get hdd temp, format for email
#
output = subprocess.check_output('sudo hddtemp /dev/sda /dev/sdb /dev/sdc', shell=True)
text = output.decode('utf-8')

#
# Email requires ascii
#
text = text.encode('ascii','ignore')
text = text.decode('ascii')

#
# Add descriptive information to text
#
text += "\nHostname: " + os.uname().nodename

#
# Call sendAlert function
#
emailgen.sendAlert(recipient, subject, text, sender, password)
