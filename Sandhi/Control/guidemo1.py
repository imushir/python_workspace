import sys
from Tkinter import *    #widgeet  classes
from types import *  #type constants
from types import ListType

class GuiMaker(Frame):
    
    menuBar = []   #class defaults
    toolBar = [] #change per instance in subclasses
    helpButton = 1 #set these in start() if need self
    
    def __init__(self,parent=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES,fill=BOTH)
        self.start()
        self.makeMenuBar()
        self.makeToolBar()
        self.makeWidgets()
    
    def makeMenuBar(self):
        """
        
        make menu bar at the top (Tk8.0 menu below)
        expand=no, fill=x so same width on resize
        """
        
        menubar = Frame(self,relief=RAISED,bd=2)
        menubar.pack(side=TOP,fill=X)
        
        for (name,key,items) in self.menuBar:
            mbutton = Menubutton(menubar,text=name,underline=key)
            mbutton.pack(side=LEFT)
            pulldown = Menu(mbutton)
            self.addMenuItems(pulldown,items)
            mbutton.config(menu=pulldown)
        
        if self.helpButton:
            Button(menubar,text = 'Help',cursor = 'gumby',relief = FLAT,command = self.help).pack(side=RIGHT)
            
    def addMenuItems(self,menu,items):
         for item in items:                 #scan nested items list
             if item == 'separator':        #string:add separator
                 menu.add_separator({})
             elif type(item) == ListType:   #list:disabled item list
                 for num in item:
                     menu.entryconfig(num,state=DISABLED)
             elif type(item[2]) != ListType:
                 menu.add_command(label = item[0],underline = item[1],command = item[2]) #cmd=callable
             else:
                 pullover = Menu(menu)
                 self.addMenuItems(pullover,item[2]) #sublist
                 menu.add_cascade(label = item[0],underline = item[1],menu = pullover) #make submenu & add cascad                 
    
    def makeToolBar(self):
        """
        make button bar at bottom,if any expand=no,fill=x so same width on resize
        """
        if self.toolbar:
            toolbar = Frame(self,cursor='hand2',relief=SUNKEN,bd=2)
            toolbar.pack(side=BOTTOM,fill=X)
            for(name,action,where) in self.toolBar:
                Button(toolbar,text=name,command=action).pack(where)
    
    def makeWidgets(self):
        """
        make 'middle' part last, so menu/toolbar
        is always on top/bottom and clipped last;
        override this default,pack middle any side;
        for grid: grid middle part in packed frame
        """
        name = Label(self,width=40,height=10,relief=SUNKEN,bg='white',text = self.__class__.__name__,cursor = 'crosshair')
        name.pack(expand=YES,fill=BOTH,side=TOP)
        
    def help(self):
        """
        override me in subclass
        """
        from tkMessageBox import showinfo
        showinfo('Help','Sorry,no help for ' +self.__class__.___name__)
    
    def start(self): pass #override me in subclass    
       
        
        
        