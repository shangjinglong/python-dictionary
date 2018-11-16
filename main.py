#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wx
import os
from database import DB
from dictionary import Dictionary
from message import Message

class MyApp(wx.App):
    def __init__(self):
        wx.App.__init__(self)
        frame = wx.Frame(parent=None,title='数据库字典生成工具V1.0',size=(420,320))

        panel = wx.Panel(frame,-1)

        wx.StaticText(panel,-1,"Host:", pos=(80,40))
        wx.StaticText(panel,-1,"Port:", pos=(80,80))
        wx.StaticText(panel, -1, "User:", pos=(80, 120))
        wx.StaticText(panel, -1, "Pass:", pos=(80, 160))
        wx.StaticText(panel, -1, "DB:", pos=(80, 200))

        self.text_host = wx.TextCtrl(panel, -1, size=(200, 30), pos=(130, 40),value="localhost")

        self.text_port = wx.TextCtrl(panel, -1, size=(200, 30), pos=(130, 80),value="3306")

        self.text_user = wx.TextCtrl(panel, -1, size=(200, 30), pos=(130, 120),value="root")

        self.text_pass = wx.TextCtrl(panel,-1, size=(200,30), pos=(130,160),value="123456")

        self.text_db =  wx.TextCtrl(panel,-1, size=(200,30), pos=(130,200),value="test")

        self.btn_generate = wx.Button(panel,-1,"生成", size=(200,50), pos=(120,240))


        self.Bind(wx.EVT_BUTTON,self.on_generate,self.btn_generate)

        frame.Center()
        frame.Show(True)


    def on_generate(self,event):
        #连接到本地数据库


        host = self.text_host.GetValue()
        port =  self.text_port.GetValue()
        user = self.text_user.GetValue()
        psw = self.text_pass.GetValue()
        database = self.text_db.GetValue()

        if host and port and user and psw and database:
            db = DB(user, psw, host, port,database)
            #print(db)
            dict = Dictionary(db)
            result = dict.getDBDoc()

            dialog = wx.DirDialog(None, '选择文件保存目录: ',
                                  style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
            if dialog.ShowModal() == wx.ID_OK:

                path = dialog.GetPath()

                #htmlFilePath = os.path.abspath(os.curdir)+'/'+self.db.database+'/dictionary.html'
                htmlFilePath = path+ '/dictionary.html'

                f = open(htmlFilePath, 'w')
                f.write(result)
                f.close()
                #docFilePath = os.path.abspath(os.curdir)+'/'+self.db.database+'/dictionary.doc'
                docFilePath = path + '/dictionary.doc'

                f = open(docFilePath, 'w')
                f.write(result)
                f.close()

                #xlsFilePath = os.path.abspath(os.curdir) +'/'+self.db.database+ '/dictionary.xls'
                xlsFilePath = path + '/dictionary.xls'

                f = open(xlsFilePath, 'w')
                f.write(result)
                f.close()

            if result:
                Message.show_message(word='数据库字典生成成功!')
                dialog.Destroy()
            else:
                Message.show_message(word="生成失败！")

        else:
            Message.show_message(word='配置信息不能为空')

if __name__=='__main__':
    app = MyApp()
    app.MainLoop()