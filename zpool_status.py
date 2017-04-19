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
subject = "zpool alert"

#
# Get zpool status, format for email
#
output = subprocess.check_output('sudo zpool status', shell=True)
text = output.decode('ascii')

#
# Add descriptive information to text
#
text += "\nHostname: " + os.uname().nodename

#
# Call sendAlert function
#
emailgen.sendAlert(recipient, subject, text, sender, password)
