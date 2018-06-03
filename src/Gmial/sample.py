
import sys
sys.path.append('/virtual/hirabayashi/module/pythonrs')

import smtplib
from email.mime.text import MIMEText as text
from email.utils import formatdate as fmt

FROM_ADDRESS = 'btpark.ryo@gmail.com'
MY_PASSWORD = 'myy623326'
TO_ADDRESS = 'ryo662233@gmail.com'
SUBJECT = 'GmailのSMTPサーバ経由'
BODY = 'pythonでメール送信'

def create_message(from_addr, to_addr, subject, body):
    msg = text(body)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Date'] = fmt()
    return msg

def send(from_addr, to_addr, msg):
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpobj.ehlo()
    smtpobj.starttls()
    smtpobj.ehlo()
    smtpobj.login(FROM_ADDRESS, MY_PASSWORD)
    smtpobj.sendmail(from_addr, to_addr, msg.as_string())
    smtpobj.close()

if __name__  == '__main__':
    msg = create_message(FROM_ADDRESS, TO_ADDRESS, SUBJECT, BODY)
    print(msg.as_string())
    send(FROM_ADDRESS, TO_ADDRESS, msg)

