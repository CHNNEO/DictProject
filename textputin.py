#from pymysql import *
import pymysql
import re

#1.创建数据库链接对象
#conn = pymysql.connect(host="localhost",user="root",
       #password="123456",database="db3",charset="utf8")
conn = pymysql.connect(host='localhost',user='root',
    password='123456',database='DictProject',charset = 'utf8')
#２．创建游标对象
cursor1 = conn.cursor()
#3.利用execute方法执行sql命令
f = open('dict.txt')
#pattern = r'\S+'
#@regex = re.compile(pattern)
for line in f:
    ss = re.split(r'[ ]+',line)
    word = ss[0]
    interpret = " ".join(ss[1:])
    try:
        sql="insert into words (word,interpret) \
        values('%s','%s');"% (word,interpret)
        cursor1.execute(sql)
        conn.commit()
    except:
        conn.rollback()
f.close()
cursor1.close()
conn.close()

