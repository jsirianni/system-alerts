#!/usr/bin/env python3
import os
import emailgen

#
# Test script for sending emails
#

recipient = input("recipient: ")
subject = input("subject: ")
body = input("message: ")
sender = input("sender: ")
password = input("sender password: ")

emailgen.sendAlert(recipient, subject, body, sender, password)
