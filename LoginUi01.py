"""
用户运行客户端即进入一级界面（登入，注册，退出)
"""
import os,sys
#import signal
from socket import *
import re


#登入功能
def login(s):
    while True:
        #请输入用户名和密码
        name = input("请输入用户名:")
        #s = name.split(" ")
        passwd = input("请输入密码:")
        msg="DLNA "+name+" "+passwd
        s.send(msg.encode())
        data = s.recv(1024).decode()
        datalist=data.split(" ")
        if datalist[0] =="OK":
            print("登入成功")
            #进入二级界面
        else:
            print("输入有误请重新输入")


#注册功能
def regist(s):
    while True:
        #请输入用户名和密码
        name = input("请输入用户名:")
        #s = name.split(" ")
        passwd = input("请输入密码:")
        msg="ZCNA "+name+" "+passwd
        s.send(msg.encode())
        data = s.recv(1024).decode()
        datalist=data.split(" ")
        if datalist[0] =="OK":
            break
        else:
            print("输入的用户名重复,请重新输入")
#服务器地址
HOST = '176.140.15.91'
PORT = 8888
ADDR = (HOST,PORT)
s = socket()
s.connect(ADDR)
#打印一级界面
while True:
    #打印一级界面
    print("=======这是一级界面请选择功能======")
    print("============1.登入=============")
    print("============2.注册=============")
    print("============3.退出=============")
    text = input("")
    if text =='1':
        login(s)
    elif text =='2':
        regist(s)
    elif text =='3':
        print("退出")
        break
    else:
        print("输入有误请重新输入")


