#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup as bs
import pickle
from gmail_log import send_mail

def main():
    old = pickle.load(open("/FULLPATH/most_recent_page.p", "rb"))
    frank = 'https://www.blonded.co'
    recent = get_page(frank)
    pickle.dump(recent,open("/FULLPATH/most_recent_page.p", "wb"))

    if old != recent:
        diff = [s for s in recent if s not in old]
        send_alert("\n".join(diff))

def get_page(p):
    page = requests.get(p)
    soup = bs(page.text, 'html.parser')
    page_str = soup.prettify()
    page_str = page_str.splitlines()
    return [s for s in page_str if 'token' not in s and 'sha256' not in s and 'Token' not in s and 'reqid' not in s]

def send_alert(mess):
    sender = 'fake.email@gmail.com'
    receivers1 = ['fake.email@gmail.com']
    receivers = ['fake.email@gmail.com']

    sub = 'BLONDED.CO CHANGED!!'
    body = 'time to start your day bruh'
    sub2 = 'blonded.co difference'
    body2 = """difference:


    """+mess

    message1 = 'Subject: {}\n\n{}'.format(sub, body)
    message2 = 'Subject: {}\n\n{}'.format(sub2, body2)
    send_mail(sender, receivers1, message1)
    send_mail(sender, receivers, message2)

if __name__ == "__main__":
    main()

