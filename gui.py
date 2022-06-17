
from tkinter import *
from tkinter import messagebox as mb

from PIL import Image,ImageTk

from guiclass import *

from tkinter import filedialog as fd

font="Times New Roman"

def setMode(mode):
    global color
    if mode.upper()== "DARK":
        color=DarkMode()
    elif mode.upper()=="LIGHT":
        color=LightMode()
    
    #print(color.getColors())
    
    
def changeMode(*args):
    for i in args:
        if type(i)==Label:
            i.config(fg=color.labelfg,
            bg=color.labelbg,)
        elif type(i)==Button:
            i.config(fg=color.labelfg,bg=color.buttons)
        elif type(i)==Entry:
            i.config(fg=color.labelfg,bg=color.entry)
        elif type(i)==Menu:
            i.config(bg=color.labelbg,fg=color.labelfg)
        elif type(i)==Frame:
            i.config(bg=color.labelbg)
        elif type(i)==Text:
            i.config(fg=color.labelfg, bg=color.entry,insertbackground=color.labelfg)
        

setMode("LIGHT")

def hide(*args):
    for i in args:
        i.pack_forget()
    

def main():
    r=tkObject("Encryption","1300x600",(500,500))
    root=r.getObject()
    
    

    r.setBg(color)
    

    def dark():
        setMode("DARK")
        r.setBg(color)
        changeMode(
            mybtn,
            header,
            menubar,
            filemenu,
            mode,
            mybtn3,
            home_btn,
            Open_btn,
            textarea_btn,
            encrypt_btn,
            decrypt_btn,
            frame,
            text,
            frame2,

            )
        mybtn.config(command=light)

        

    def light():
        setMode("LIGHT")
        r.setBg(color)
        changeMode(
            mybtn,
            header,
            menubar,
            filemenu,
            mode,
            mybtn3,
            home_btn,
            textarea_btn,
            encrypt_btn,
            decrypt_btn,
            frame,
            text,
            frame2,

            )
        mybtn.config(command=dark)

    def activateText():
        frame2.pack(side=TOP)

        
    frame=Frame(bg=color.labelbg)
    frame2=Frame(root,bg=color.labelbg,width=1400,height=600)
    frame.pack(side=TOP)
    
    myimg= PhotoImage(file="icons8-data-encryption-100.png")
    p= myimg.subsample(3,3)

    header=Label(
        frame,
        text="ENCRYPTION SYSTEM",
        font=(font,20,"bold"),
        padx=10,
        pady=3,
        bg=color.labelbg,
        fg= color.labelfg,
        image=p,
        compound= LEFT,
        relief=RAISED
    )
    header.pack(side=LEFT,fill=X)


    myimg5= PhotoImage(file="icons8-close-100.png")
    p5= myimg5.subsample(3,3)
    mybtn3=Button(
        frame,
        command=lambda:root.destroy(),
        bg=color.buttons,
        fg=color.labelfg,
        font= (font,12,"bold"),
        padx=5,pady=2,
        image=p5,
        compound=LEFT,
        )
    mybtn3.pack(side=RIGHT)
    CreateToolTip(mybtn3,"close window")


         
        
    myimg2= PhotoImage(file="icons8-invert-colors-100.png")
    p2= myimg2.subsample(3,3)
    mybtn=Button(
        frame,
        command=lambda:light(),
        bg=color.buttons,
        fg=color.labelfg,
        font= (font,12,"bold"),
        padx=5,pady=2,
        image=p2,
        compound=LEFT,
        
        
        )
    mybtn.pack(side=RIGHT)
    CreateToolTip(mybtn,"change mode")

    myimg14= PhotoImage(file="icons8-data-encryption-100.png")
    p14= myimg14.subsample(3,3)
    decrypt_btn=Button(
        frame,
        command=lambda:None,
        bg=color.buttons,
        fg=color.labelfg,
        font= (font,12,"bold"),
        padx=5,pady=2,
        image=p14,
        compound=LEFT,
        )
    decrypt_btn.pack(side=RIGHT)
    CreateToolTip(decrypt_btn,"Decrypt")

    myimg15= PhotoImage(file="icons8-data-protection-100.png")
    p15= myimg15.subsample(3,3)
    encrypt_btn=Button(
        frame,
        command=lambda:None,
        bg=color.buttons,
        fg=color.labelfg,
        font= (font,12,"bold"),
        padx=5,pady=2,
        image=p15,
        compound=LEFT,
        )
    encrypt_btn.pack(side=RIGHT)
    CreateToolTip(encrypt_btn,"Encrypt")
   

    
    myimg17= PhotoImage(file="icons8-align-text-left-100.png")
    p17= myimg17.subsample(3,3)
    textarea_btn=Button(
        frame,
        command=lambda:activateText(),
        bg=color.buttons,
        fg=color.labelfg,
        font= (font,12,"bold"),
        padx=5,pady=2,
        image=p17,
        compound=LEFT,
        )
    textarea_btn.pack(side=RIGHT)
    CreateToolTip(textarea_btn,"Text Area")


    myimg11= PhotoImage(file="icons8-open-view-100.png")
    p11= myimg11.subsample(3,3)
    Open_btn=Button(
        frame,
        command=lambda:None,
        bg=color.buttons,
        fg=color.labelfg,
        font= (font,12,"bold"),
        padx=5,pady=2,
        image=p11,
        compound=LEFT,
        )
    Open_btn.pack(side=RIGHT)
    CreateToolTip(Open_btn,"Open File")
    myimg8= PhotoImage(file="icons8-home-100.png")
    p8= myimg8.subsample(3,3)
    home_btn=Button(
        frame,
        command=lambda:[root.destroy(),main()],
        bg=color.buttons,
        fg=color.labelfg,
        font= (font,12,"bold"),
        padx=5,pady=2,
        image=p8,
        compound=LEFT,
        )
    home_btn.pack(side=RIGHT)
    CreateToolTip(home_btn,"Home")
    
    
    global text
    text=Text (
        frame2,
        width=500,
        fg=color.labelfg,
        bg=color.entry,
        cursor="arrow",
        insertbackground=color.labelfg,
        font=(font,12,"normal"),
        
        
    )
    
    s=Scrollbar(frame2)
    s.pack(side=RIGHT,fill=Y)
    text.config(yscrollcommand = s.set)
    text.pack(side=TOP,fill=BOTH,expand=TRUE )
    # frame2.pack(side=TOP)


    menubar=Menu(root)
    filemenu = Menu(menubar, tearoff=0,bg=color.labelbg,fg= color.labelfg,relief=RAISED,font=(font,12,"normal"))
    menubar.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="Encrypt File",command=None)
    filemenu.add_command(label="Decrypt File",command=None)

    mode=Menu(menubar,tearoff=0,bg=color.labelbg,fg= color.labelfg,relief=RAISED,font=(font,12,"normal"))
    menubar.add_cascade(label="Change Mode",menu=mode)
    mode.add_command(label="Light Mode",command =light)
    mode.add_command(label="Dark Mode",command =dark)

    help=Menu(menubar,tearoff=0,bg=color.labelbg,fg= color.labelfg,relief=RAISED,font=(font,12,"normal"))
    menubar.add_cascade(label="Help", menu=help)
    help.add_command(label="Help",command=None)
    help.add_command(label="How it works?",command=None)
    help.add_command(label="FAQs",command=None)
    
    root.config(menu=menubar)


    r.getMainloop()




main()














