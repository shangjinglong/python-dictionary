#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx

class Message:

    @staticmethod
    def show_message(word):
        dlg = wx.MessageDialog(None, word, u"操作提示", wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            # self.Close(True)
            pass
        dlg.Destroy()

