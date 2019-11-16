#!/usr/bin/python3
import smtplib
import base64
def send_mail(sent_from, to, email_text):
    try:
        #Log onto gmail
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()

        #lol password
        gmail_user = 'fake.email@gmail.com'
        gmail_password = base64.b64decode(b'fake.password').decode('utf-8')

        #log onto my account
        server.login(gmail_user, gmail_password)

        #send da mail
        server.sendmail(sent_from, to, email_text)
        server.close()

    except:
        print('Error: Cannot send email')
if __name__ == "__main__":
    sender = 'fake.email@gmail.com'
    receivers = ['fake.email@gmail.com']
    sub = 'cron tab worked'
    body = 'cron worked'
    message1 = 'Subject: {}\n\n{}'.format(sub, body)
    send_mail(sender, receivers, message1)
