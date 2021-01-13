#!/usr/bin/env python3

import smtplib
import email.mime.text
import syslog
import datetime
import subprocess
import time

GMAIL_ADDRESS = 'XXXXXX'
GMAIL_PASSWORD = 'XXXXXX'
to_emails = [""]  # cell phone address

syslog.openlog('[UPS]')
def log(msg):
    syslog.syslog(str(msg))

def getApcStatus():
    apcStatus = subprocess.run(['/sbin/apcaccess', 'status'], stdout=subprocess.PIPE)
    apcStatList = apcStatus.stdout.decode('utf-8').split('\n')

    apcStats = {}
    for r in apcStatList:
        if r:
            a,b = r.split(':', 1)
            apcStats[a.strip()] = b.strip()
    return apcStats

def sendSms(text=None,subject=None):
    s = datetime.datetime.today().isoformat()
    s = s[:s.index('.')].replace('T', ' ')

    msg_subject=subject
    msg_text = s
    if text:
        msg_text = msg_text + ": " + text

    log(msg_subject)

    msg = email.mime.text.MIMEText(msg_text)
    msg['Subject'] = msg_subject
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    s = smtplib.SMTP_SSL('smtp.gmail.com', '465')
    s.login(GMAIL_ADDRESS, GMAIL_PASSWORD)
    s.sendmail(from_email, to_emails, msg.as_string())
    s.quit()

from_email = GMAIL_ADDRESS

def main():
    msg_subject = "ALERT: UPS On battery Power"
    sendSms(None,msg_subject)
    time.sleep(30)

    while True:
        apcStats = getApcStatus()
        msg = "\nBattery Percentage: %s\nTime Remaining: %s\nCurrent Load: %s" % ( apcStats['BCHARGE'], apcStats['TIMELEFT'], apcStats['LOADPCT'])
        sendSms(msg)
        time.sleep(120)

if __name__ == "__main__":
    main()
