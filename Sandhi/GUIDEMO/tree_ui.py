#!/usr/bin/python
import wx
from time import *

class MyFrame(wx.Frame):
    def __init__(self,parent,id,title):
        wx.Frame.__init__(self,parent,id,title,wx.DefaultPosition, (550,350))
        zone_list = ['CET','GMT','MSK','EST','PST','EDT']
        self.full_list = {'CET': 'Central European Time','GMT': 'Greenwich Mean Time','MSK': 'Moscow Time','EST': 'Eastern Standard Time','PST': 'Pacific Standard Time','EDT':'Eastern Daylight Time' }
        self.time_diff = {'CET' : 1,'GMT' : 0,'MSK': 3,'EST':-5,'PST':-8,'EDT':-4}
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.timer = wx.Timer(self,1)
        self.diff  = 0
        panel = wx.Panel(self,-1)
        self.time_zones = wx.ListBox(panel,26,wx.DefaultPosition,(170,130),zone_list,wx.LB_SINGLE)
        self.text = wx.TextCtrl(panel,-1,'Central European Time',size=(200,130),style=wx.TE_MULTILINE)
        self.time = wx.StaticText(panel,-1,'')
        btn = wx.Button(panel,wx.ID_CLOSE,'Close')
        hbox1.Add(self.time_zones,0,wx.TOP,40)
        hbox1.Add(self.text,1,wx.LEFT | wx.TOP,40)
        hbox2.Add(self.time,1,wx.ALIGN_CENTER)
        hbox3.Add(btn,0,wx.ALIGN_CENTER)
        vbox.Add(hbox1,0,wx.ALIGN_CENTER)
        vbox.Add(hbox2,1,wx.ALIGN_CENTER)
        vbox.Add(hbox3,1,wx.ALIGN_CENTER)
        panel.SetSizer(vbox)
        self.timer.Start(100)
        self.Bind(wx.EVT_BUTTON,self.OnClose,id=wx.ID_CLOSE)
        self.Bind(wx.EVT_LISTBOX,self.OnSelect,id=26)
        self.Bind(wx.EVT_TIMER,self.OnTimer,id=1)
        
        def OnClose(self,event):
            self.Close()
        
        def OnSelect(self,event):
            index = event.GetSelection()
            time_zone = self.time_zones.GetString(index)
            self.diff = self.time_diff[time_zone]
            self.text.SetValue(self.full_list[time_zone])
        
        def OnTimer(self,event):
            ct = gmtime()
            print_time = (ct[0],ct[1],ct[2,ct[3]+self.diff,ct[4],ct[5],ct[6],ct[7],-1])
            self.time.SetLabel(strftime("%H:%M:%S",print_time))
class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None,-1,'ListBoxDemo')
        frame.Centre()
        frame.Show(True)
        return True

app = MyApp(0)
app.MainLoop()    