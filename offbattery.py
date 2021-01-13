#!/usr/bin/env python3

import smtplib
import email.mime.text
import syslog
import datetime
import subprocess

GMAIL_ADDRESS = 'XXXXXX'
GMAIL_PASSWORD = 'XXXXXXX'
to_emails = [""]  # cell phone address

# Kill off the running textStatus.py script (forked in background)
running = subprocess.run(['ps','a','u','x'], stdout=subprocess.PIPE).stdout.decode('utf-8').splitlines()
killIt = None
for r in running:
    if 'textStatus' in r:
        killIt = r.split()[1]
if killIt:
    subprocess.run(['kill','-9',killIt])

syslog.openlog('[UPS]')
def log(msg):
    syslog.syslog(str(msg))

from_email = GMAIL_ADDRESS

s = datetime.datetime.today().isoformat()
s = s[:s.index('.')].replace('T', ' ')

msg_subject = "ALERT: UPS Back On Line Power"
msg_text = s

log(msg_subject)

msg = email.mime.text.MIMEText(msg_text)
msg['Subject'] = msg_subject
msg['From'] = from_email
msg['To'] = ", ".join(to_emails)
s = smtplib.SMTP_SSL('smtp.gmail.com', '465')
s.login(GMAIL_ADDRESS, GMAIL_PASSWORD)
s.sendmail(from_email, to_emails, msg.as_string())
s.quit()
