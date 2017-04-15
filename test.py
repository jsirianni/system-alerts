#!/usr/bin/env python3
import os
import email_gen

#
# Test script for sending emails
#

recipient = input("recipient: ")
subject = input("subject: ")
body = input("subject: ")

email_gen(recipient, subject, body)
