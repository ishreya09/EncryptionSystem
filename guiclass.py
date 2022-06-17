
from tkinter import *

class Colors:
    
    def __init__(self,mode):
        
        #defining all colors here
        if mode.lower()=='dark':
            self.mode= "DARK"
        elif mode.lower()=='light':
            self.mode= "LIGHT"
        else:
            self.mode="DEFAULT"

    
    def set_colors(self,header,buttons,background,labelbg,labelfg,entry):
        self.header=header
        self.buttons=buttons
        self.background=background
        self.labelbg=labelbg
        self.labelfg=labelfg
        self.entry=entry

    def getMode(self):
        return self.mode

    def setMode(self,mode):
        self.__init__(self,self.object,mode)

    def changeMode(self,mode):
        if mode.upper()=="DARK":
            return DarkMode(self)
        elif mode.upper()=="LIGHT":
            return LightMode(self)
        else :
            return DefaultMode(self)
    
    def getBg(self):
        return self.background
    
    
    
class DarkMode(Colors):
    def __init__(self,header="#0a0a0f",buttons="#33334d",background="#3d3d5c",labelbg="#3d3d5c",labelfg="white",entry="#0a0a0f"):
        Colors.__init__(self,"DARK")
        
        self.header=header
        self.buttons=buttons
        self.background=background
        self.labelbg=labelbg
        self.labelfg=labelfg
        self.entry=entry
        self.set_colors()
    
    def getColors(self):
        return self.header, self.buttons,self.background,self.labelfg,self.labelbg,self.entry
    
    def set_colors(self, header="#0a0a0f",buttons="#33334d",background="#3d3d5c",labelbg="#3d3d5c",labelfg="white",entry="#0a0a0f"):
        return super().set_colors(header, buttons, background, labelbg, labelfg, entry)
    
class LightMode(Colors):
    def __init__(self,header="#d9d9d9",buttons="#0099ff",background="#66ccff",labelbg="#66ccff",labelfg="black",entry="white"):
        Colors.__init__(self,"LIGHT")
        
        self.header=header
        self.buttons=buttons
        self.background=background
        self.labelbg=labelbg
        self.labelfg=labelfg
        self.entry=entry

    def getColors(self):
        return self.header, self.buttons,self.background,self.labelfg,self.labelbg,self.entry
    
    def set_colors(self, header="#d9d9d9", buttons="#0099ff", background="#66ccff", labelbg="#66ccff", labelfg="black", entry="white"):
        return super().set_colors(header, buttons, background, labelbg, labelfg, entry)

class DefaultMode(Colors):
    def __init__(self,header,buttons,background,labelbg,labelfg,entry):
        Colors.__init__(self,"DEFAULT")
        
        self.buttons=buttons
        self.background=background
        self.labelbg=labelbg
        self.labelfg=labelfg
        self.entry=entry
        self.set_colors()

    def getColors(self):
        return self.header, self.buttons,self.background,self.labelfg,self.labelbg,self.entry

    def set_colors(self, header, buttons, background, labelbg, labelfg, entry):
        return super().set_colors(header, buttons, background, labelbg, labelfg, entry)

"""
class Mode(DarkMode or LightMode or DefaultMode):
    def __init__(self,mode):
        Colors.__init__(self,mode)
        if self.getMode()=="DARK":
            DarkMode.__init__(self)
        elif self.getMode()=="LIGHT":
            LightMode.__init__(self)
        else:
            DefaultMode.__init__(self)
"""



class tkObject:
    def __init__(self,title,geometry,min):
        self.title= title
        #self.bg=bg
        self.geometry = geometry
        self.minsize= min
        self.object=Tk()
        self.__createWindow()
        

    def __createWindow(self):
        self.object.geometry(self.geometry)
        self.object.title(self.title)
        self.object.minsize(self.minsize[0],self.minsize[1])
        # self.object.iconbitmap("icons8-data-protection-100.png")
        #self.object.config(bg=self.bg)

    def setBg(self,colorObject:Colors):
        self.object.config(bg=colorObject.getBg())

    def setObject(self,title,bg,geometry,min):
        self.__init__(title,bg,geometry,min)

    def getObject(self):
        return self.object

    def getMainloop(self):
        self.object.mainloop()
          
import re

class HoverInfo(Menu):
    def __init__(self, parent, text, command=None):
        self._com = command
        Menu.__init__(self,parent, tearoff=0)
        if not isinstance(text, str):
            raise TypeError('Trying to initialise a Hover Menu with a non string type: ' + text.__class__.__name__)
        toktext=re.split('\n', text)
        for t in toktext:
            self.add_command(label = t)
            self._displayed=False
            self.master.bind("<Enter>",self.Display )
            self.master.bind("<Leave>",self.Remove )
    
    def __del__(self):
        self.master.unbind("<Enter>")
        self.master.unbind("<Leave>")
 
    def Display(self,event):
        if not self._displayed:
            self._displayed=True
            self.post(event.x_root, event.y_root)
        if self._com != None:
            self.master.unbind_all("<Return>")
            self.master.bind_all("<Return>", self.Click)
 
    def Remove(self, event):
        if self._displayed:
            self._displayed=False
            self.unpost()
        if self._com != None:
            self.unbind_all("<Return>")
        
    def Click(self, event):
        self._com()

class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("Times New Roman", "10", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)



