#!/usr/bin/env python3
import os
import subprocess
import emailgen
import subprocess
from email.mime.text import MIMEText

#
# Test script for sending emails
#
recipient = input("recipient: ")
subject = input("subject: ")
sender = input("sender: ")
password = input("sender password: ")


output = subprocess.check_output('sudo zpool status', shell=True)
body = MIMEText(output)
text = str(body)

emailgen.sendAlert(recipient, subject, text, sender, password)
