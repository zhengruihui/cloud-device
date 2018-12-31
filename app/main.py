#!/usr/bin/python
# -*- coding: UTF-8 -*-

# from poplib import POP3
# import time
#
# while True:
#     time.sleep(0.1)
#
#     M = POP3('pop.163.com')
#     M.user('18966166778@163.com')
#     M.pass_('Melody3058')
#
#     numMessages = len(M.list()[1])
#     for i in range(numMessages):
#         for j in M.retr(i+1)[1]:
#             # if j == "Subject: 1":
#             if j.find("Subject: 1"):
#                 print("1")


import poplib

# 输入邮件地址, 口令和POP3服务器地址:
email = '18966166778@163.com'
password = 'Melody3058'
pop3_server = 'pop.163.com'

# 连接到POP3服务器:
server = poplib.POP3(pop3_server)
# 可以打开或关闭调试信息:
# server.set_debuglevel(1)
# 可选:打印POP3服务器的欢迎文字:
print(server.getwelcome())
# 身份认证:
server.user(email)
server.pass_(password)
# stat()返回邮件数量和占用空间:
print('Messages: %s. Size: %s' % server.stat())
# list()返回所有邮件的编号:
new_index = 0
while True:
    resp, mails, octets = server.list()
    # 可以查看返回的列表类似['1 82923', '2 2184', ...]
    # print(mails)
    # 获取最新一封邮件, 注意索引号从1开始:
    index = len(mails)
    if not new_index == index:
        resp, lines, octets = server.retr(index)
        new_index = index
        print("got new")
print("done")
