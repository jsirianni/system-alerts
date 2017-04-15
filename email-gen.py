#!/usr/bin/env python3
import smtplib


def sendAlert(recipient, subject, text):
'''
Call this function to send an alert via gmail
Sending email account and password is predefined
Pass a recipient email address, subject, message to send (text)
'''

    TO = 'recipient@mailservice.com'
    SUBJECT = 'TEST MAIL'
    TEXT = 'Here is a message from python.'

    #Gmail Sign In
    gmail_sender = 'sender@gmail.com'
    gmail_passwd = 'password'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_sender, gmail_passwd)

    BODY = '\r\n'.join(['To: %s' % TO,
                        'From: %s' % gmail_sender,
                        'Subject: %s' % SUBJECT,
                        '', TEXT])

    try:
        server.sendmail(gmail_sender, [TO], BODY)
        print ('email sent')
    except:
        print ('error sending mail')

    server.quit()
