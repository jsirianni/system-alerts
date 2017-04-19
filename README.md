#### System Alerts v1.0.0

#### Description
This repo provides a framework to quickly integrate SMTP email alerts into your program using Python 3.

#### How it works
emailgen.py has a function called 'sendAlert'

The sendAlert function should be passed five strings in this order
  - recipient email address (Can be your real email address)
  - subject
  - message (output from a command run from cron for example)
  - sending email address (should be a throw away email)
  - sending email password (Stored in plain text!)

Several example scripts are provided
  - text.py: Prompts user for input, sends email
  - zpool_status.py: Prompts user for input, sends output of zpool status
  - hddtempalert.py: Prompts user for input, sends output of hddtemp
    - Edit this script to reflect drives to check

#### Supported OS
- Debian 9 w/ Python 3
- Ubuntu 16.04 w/ Python 3
