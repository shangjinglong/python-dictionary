#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector
from message import Message

class DB:
    host = 'localhost'
    user = 'root'
    port = 3306
    password = '123456'
    database = 'test'
    conn =''
    def __init__(self,user='',password='',host='',port='',database=''):
        if host :
            self.host = host
        if user :
            self.user = user
        if password :
            self.password = password
        if database :
            self.database = database
        if port:
            self.port = port
        try:
            self.conn = mysql.connector.connect(user=self.user, password=self.password,host=self.host,port=self.port, database=self.database, charset='utf8')
        except Exception as e:
            Message.show_message(str(e))

    def query(self,sql):
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except Exception as e:
            Message.show_message(str(e))


