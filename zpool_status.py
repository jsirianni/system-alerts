#!/usr/bin/env python3
import os
import subprocess
import emailgen

#
# Test script for sending emails
#

recipient = input("recipient: ")
subject = input("subject: ")
sender = input("sender: ")
password = input("sender password: ")


import subprocess
body = subprocess.check_output('sudo zpool status', shell=True)

text = str(body)

emailgen.sendAlert(recipient, subject, text, sender, password)
