#!/usr/bin/env python3
import os
import subprocess
import emailgen
#
# Check MDADM STATUS, run via cron
#


#
# Get MDADM status
#
status = subprocess.check_output("sudo mdadm --detail /dev/md129 | grep 'State :'", shell=True)
status = status.decode('ascii')


#
# Parse string, if DEGRADED then call email script
#
if " degr" in status:
    # Header information
    recipient = ""
    sender = ""
    password = ""
    subject = "MDADM is DEGRADED: " + os.uname().nodename

    # Get MDADM status, format for email
    output = subprocess.check_output('sudo mdadm --detail /dev/md*', shell=True)
    text = output.decode('ascii')

    # Add descriptive information to text
    text += "\nHostname: " + os.uname().nodename

    # Call sendAlert function
    emailgen.sendAlert(recipient, subject, text, sender, password)


else:
    print("MDADM IS HEALTHY")
