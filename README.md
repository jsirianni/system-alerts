#### System Alerts v0.0.1

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

Currently emailgen.py has email addresses and passwords hardcoded. This will be fixed in a later release.

To test this program, run test.py.


#### Supported OS
- Debian 9 w/ Python 3

