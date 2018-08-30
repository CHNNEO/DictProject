#!/usr/bin/env python3
#coding=utf-8

from socket import *
import os 
import signal
import time 
import sys
import pymysql
from pymsql import *

HOST = '127.0.0.1'
PORT = 8888
ADDR = (HOST,PORT)

#主控流程
def main():
    #数据库连接
    db = pymysql.connect('localhost','root','123456','DictProject')
    #创建TCP套接字
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    while True:
        try:
            c,addr = s.accept()
            print("Connect from",addr)
        except KeyboardInterrupt:
            sys.exit("服务退出")
        except Exception :
            continue
        #创建子进程
        pid = os.fork()
        if pid < 0:
            print("创建子进程失败")
        if pid == 0:
            s.close()
            do_child(c,db)
        else:
            c.close()
            continue
def do_child(c,db):
    while True:
        data = c,recv(128).decode()
        print("Request:",data)
        if data[0]=='R':
            do_register(c,db,data)
        elif data[0]=="L":
            name = do_login(c,db,data)
        elif data[0]=="E":
            c.close()
            sys.exit(0)
        elif data[0] =="Q":
            do_query(c,db,name,data)
        elif data[0] == "H":
            do_history(c,db,name)

def do_login(c,db,data):
    print("登入操作")
    l = data.split(" ")
    name =l[1]
    passwd =l[2]
    cursor = db.cursor()
    sql = "select * from user where name = '%s' and passwd ='%s';"%(name,word,tm)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        return
    sql = "select * from words where word ='%s';"%word
    try:
        cursor.execute(sql)
        r = cursor.fetchone()
    except:
        pass

    if not r:
        c.send(b"Fail")
    else:
        c.send(b"OK")
        time.sleep(0.1)
        msg = "{} : {}".format(r[1],r[2])
        c.send(msg.encode())
        insert_history()

def do_history(c,db,name):
    print("历史记录")
    cursor = db.cursor()
    sql = "select * from hist where name = '%s';"%name
    try:
        cursor.execute(sql)
        r = cursor.fetchall()
    except:
        pass
    if not r:
        c.send(b"Fail")
    else:
        c.send(b'OK')
        time.sleep(0.1)
        for i in r:
            msg="{} {} {} \n".format(i[1],i[2],i[3])
            c.send(msg.encode())
        time.sleep(0.1)
        c.send(b"##")
def do_register(c,db,data):
    print(">>>>执行注册操作<<<<<")
    l = data.split(" ")
    name = l[1]
    passwd = l[2]
    cursor = db.cursor()
    #判断name是否存在
    sql = "select name from user where name ='%s';"%name
    cursor.execute(sql)
    r = cursor.fetchone()
    if r != None:
        c.send(b'EXISTS')
        return
    #插入数据到数据库
    sql = "insert into user (name , passwd) \
    values ('%s','%s');"%(name,passwd)
    try:
        cursor.execute(sql)
        db.commit()
        c.send(b'OK')
    except:
        c.send(b'Fail')
        db.rollback()
        return
    else:
        print("注册成功")

if __name__=="__main__":
    main()
    