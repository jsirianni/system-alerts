#!/usr/bin/env python3
import os
import subprocess
import emailgen
#
# Check ZPOOL STATUS, run via cron
#


#
# Get zpool status
#
status = subprocess.check_output('sudo zpool status | grep state', shell=True)
status = status.decode('ascii')


#
# Parse string, if DEGRADED then call email script
#
if " DEGRADED" in status:
    # Header information
    recipient = ""
    sender = ""
    password = ""
    subject = "TeamIT Alerts: ZPOOL DEGRADED " + os.uname().nodename

    # Get zpool status, format for email
    output = subprocess.check_output('sudo zpool status', shell=True)
    text = output.decode('ascii')

    # Add descriptive information to text
    text += "\nHostname: " + os.uname().nodename

    # Call sendAlert function
    emailgen.sendAlert(recipient, subject, text, sender, password)

else:
    print("ZPOOL IS HEALTHY")
