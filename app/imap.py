#!/usr/bin/python
# -*- coding: UTF-8 -*-


import getpass, imaplib
import email
import time

host = 'imap.qq.com'
port = 993

M = imaplib.IMAP4_SSL(host, port)
M.login("3030613122@qq.com", "jqadfmklhpuzdddg")

result, message = M.select("INBOX", readonly=False)
print(result, message)
index = 0

while True:
    time.sleep(0.1)
    data_type, data = M.search(None, '(FROM "3030613122@qq.com")')
    newlist = data[0].split()
    newest_inedx = len(newlist)

    if not (index == newest_inedx):
        index = newest_inedx
        if index == 0:
            continue
        data_type, data = M.fetch(newlist[newest_inedx-1], '(RFC822)')
        msg = email.message_from_string(data[0][1].decode('utf-8'))
        sub = msg.get('subject')
        print(sub)


