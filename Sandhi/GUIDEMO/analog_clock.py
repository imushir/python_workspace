#!/usr/bin/python
import wx
from wx.lib import analogclock as ac
class MyFrame(wx.Frame):
    def __init__(self,parent,id,title):
        wx.Frame.__init__(self,parent,id,title)
        clock = ac.AnalogClockWindow(self)
        clock.SetBackgroundColour('gray')
        clock.SetHandColours('black')
        clock.SetTickColours('WHITE')
        clock.SetTickSizes(h=5,m=2)
        clock.SetTickStyles(ac.TICKS_ROMAN)
        self.SetSize(400,350)
class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None,-1,'analog')
        frame.Show(True)
        frame.Centre()
        return True
    
app = MyApp(0)
app.MainLoop()        
        