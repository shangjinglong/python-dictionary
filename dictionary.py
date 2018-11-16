#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QWidget

class Dictionary:
    db = ''
    def __init__(self,DB):
        self.db = DB

    def getTables(self):
        sql = 'SHOW TABLE STATUS'
        table = []
        tables = self.db.query(sql)
        #print(tables)
        for i,t in enumerate(tables):
            table.insert(i,{'table_name':t[0],'comment':t[17]})
        return table

    def getFieldsByTable(self,table):
        sql = "SELECT * FROM information_schema.`COLUMNS` WHERE TABLE_SCHEMA='"+self.db.database+"' AND TABLE_NAME='"+table+"'"
        fields = self.db.query(sql)
        return fields

    def getDbStructure(self):
        arrTables = self.getTables()

        arrDbStructure = {}
        for i,t in enumerate(arrTables):
            arrFields = self.getFieldsByTable(t.get('table_name'))

            arrTmpFields = []
            #print arrFields
            for j,f in enumerate(arrFields):
                arrTmpFields.insert(j,{'fields_name':f[3],'fields_type': f[15],'fields_comment': f[19]})
            arrDbStructure[t.get('table_name')] = arrTmpFields
            #arrDbStructure[t.get('table_name').encode('utf-8')]['comment'] = t.get('comment')
        #print arrDbStructure
        return arrDbStructure

    def getDBDoc(self):
        arrDbStructure = self.getDbStructure()

        strTable = ''
        i = 0
        for j,t in enumerate(arrDbStructure):
            i=i+1
            strTable=strTable+'<h4>No.'+'%d'%i+'--表名:'+'%s'%t+'</h4>'
            #print('No.'+'%d'%i+'--表名:'+'%s'%t+''+' 生成完毕')
            strTable=strTable+'<table border="2">'
            strTable=strTable+'<tr><th width="150px">字段名</th><th width="200px">字段类型</th><th width="850px">字段含义</th></tr>'
            fields_info = ''
            for y,x in enumerate(arrDbStructure.get(t)):
                #print(str(x.get('fields_name')))
                fields_info=fields_info+'<tr><td>'+'%s'%x.get('fields_name')+'</td><td>'+'%s'%x.get('fields_type')+'</td><td>'+'%s'%x.get('fields_comment')+'</td></tr>'
            strTable=strTable+fields_info+'</table><br><br>'
            strTable = '<!DOCTYPE html><html lang="zh-cn"><head><meta charset="utf-8" /><title>'+self.db.database+'数据字典</title></head><style type="text/css">table{border:1px solid black;border-collapse:collapse;}table, td, th{border:1px solid black;}tr{width:1200px;}td{text-align:left;padding-left:10px;}</style><body>'+strTable+'</body></html>'

        return strTable

