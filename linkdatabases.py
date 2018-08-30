#from pymysql import *
import pymysql

#1.创建数据库链接对象
#conn = pymysql.connect(host="localhost",user="root",
       #password="123456",database="db3",charset="utf8")
conn = pymysql.connect(host='localhost',user='root',
    password='123456',database='',charset = 'utf8')
#２．创建游标对象
cursor1 = conn.cursor()
#3.利用execute方法执行sql命令
try:
    create_databases = 'create database DictProject character set utf8'
    cursor1.execute(create_databases)
    conn.commit()
except Exception as e:
    conn.rollback()
    #print("出现错误，已回滚",e)
cursor1.close()
conn.close()

#重新创建数据库连接,并建立三张数据表dict_table,user_table,recode_table
conn01 = pymysql.connect(host='localhost',user='root',
    password='123456',database='DictProject',charset = 'utf8')
cursor01=conn01.cursor()
try:
    cre_tab01="create table user(id int auto_increment primary key,\
    name varchar(32) not null,passwd varchar(10) default '000000');"
    cre_tab02="create table hist(id int auto_increment primary key,\
    name varchar(32) not null,word varchar(32) not null,\
    time varchar(64) not null);"
    cre_tab03="create table words(id int auto_increment primary key,\
    word varchar(32) not null, interpret text not null);"
    cursor01.execute(cre_tab01)
    cursor01.execute(cre_tab02)
    cursor01.execute(cre_tab03)
    conn01.commit()
except Exception as e:
    conn01.rollback()
    #print("出现错误，已回滚",e)
cursor01.close()
conn01.close()
