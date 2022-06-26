
from tkinter import *
from tkinter import messagebox as mb

from PIL import Image,ImageTk

from guiclass import *

from tkinter import filedialog as fd
import function as pc

font="Times New Roman"

global key, message, address, shift

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
    
    scroll=Scrollbar(root)
    scroll.pack(side=RIGHT,fill=Y)
    # root.config(yscrollbar=s.set)

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
            frame3,
            key_label,
            key_entry,
            shift_label,
            shift_entry,
            text_label,
            text,
            s1,
            key_label1,
            key_entry1,
            shift_label1,
            shift_entry1,
            text_label1,
            text1,
            encrypt_btn_str,
            decrypt_btn_str,
            add_new_label,
            add_new_entry,
            add_new_label1,
            add_new_entry1,

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
            frame3,
            key_label,
            key_entry,
            shift_label,
            shift_entry,
            text_label,
            text,
            s1,
            key_label1,
            key_entry1,
            shift_label1,
            shift_entry1,
            text_label1,
            text1,
            encrypt_btn_str,
            decrypt_btn_str,
            add_new_label,
            add_new_entry,
            add_new_label1,
            add_new_entry1,

            )
        mybtn.config(command=dark)

    def activateText():
        frame2.pack(side=TOP)
    
    def open_file():
        
        global file_path
        file_path = fd.askopenfilename()
        # print(file_path)
        f = open(file_path, "r")
        pc.address = file_path
        message= f.read()
        text1.delete('1.0', END)
        text1.insert(END,message)
        f.close()
        frame3.pack(side=TOP)

    def encrypt_string():
        pc.text = text.get(1.0, "end-1c")
        pc.key= key_entry.get()
        pc.shift= int(shift_entry.get())
        pc.address = None
        pc.address_new= add_new_entry.get()
        pc.encrypt_string()
        
        mb.OK("The File is Encrypted","The File is Encrypted in {}".format(pc.address_new))
        frame2.pack_forget()


    def decrypt_string():
        pc.text=text.get(1.0, "end-1c")
        pc.key=key_entry.get()
        pc.shift=int(shift_entry.get())
        pc.address=None
        pc.address_new= add_new_entry.get()
        pc.decrypt_string()
        
        mb.OK("The string is decrypted", "The string is decrypted in {}".format(pc.address_new))
        frame2.pack_forget()


    def decrypt_file():
        pc.text=text1.get(1.0, "end-1c")
        pc.key=key_entry1.get()
        pc.shift=int(shift_entry1.get())
        pc.address=file_path.get()
        pc.address_new = add_new_entry1.get()
        p=pc.decrypt_file()
        mb.OK("The file is decrypted","The file is decrypted in {}".format(pc.address_new))
        frame3.pack_forget()

    def encrypt_file():
        pc.text=text1.get(1.0, "end-1c")
        pc.key=key_entry1.get()
        pc.shift=int(shift_entry1.get())
        pc.address=file_path.get()
        pc.address_new = add_new_entry1.get()
        pc.encrypt_file()
        mb.OK("The file is encrypted","The file is encrypted in {}".format(pc.address_new))
        frame3.pack_forget()


        
    frame=Frame(bg=color.labelbg)
    frame2=Frame(root,bg=color.labelbg,width=1400,height=600) # for text
    frame3=Frame(root,bg=color.labelbg,width=1400,height=600) # for file

    frame.pack(side=TOP)

    key_label = Label (
        frame2,
        text = "KEY :",
        fg=color.labelfg,
        bg=color.labelbg,
        cursor="arrow",
        font=(font,12,"normal"),
    )
    key_label.pack(side = TOP)    

    key_entry = Entry (
        frame2,
        width = 100,
        fg=color.labelfg,
        bg=color.entry,
        cursor="arrow",
        insertbackground=color.labelfg,
        font=(font,12,"normal"),
        
    )
    key_entry.pack(side =TOP,expand=True)

    shift_label = Label (
        frame2,
        text = "SHIFT :",
        fg=color.labelfg,
        bg=color.labelbg,
        cursor="arrow",
        font=(font,12,"normal"),
    )
    shift_label.pack(side = TOP)    

    shift_entry = Entry (
        frame2,
        width = 100,
        fg=color.labelfg,
        bg=color.entry,
        cursor="arrow",
        insertbackground=color.labelfg,
        font=(font,12,"normal"),
        
    )
    shift_entry.pack(side =TOP,expand=True)

    add_new_label = Label (
        frame2,
        text = "Name of the file to store in :",
        fg=color.labelfg,
        bg=color.labelbg,
        cursor="arrow",
        font=(font,12,"normal"),
    )
    add_new_label.pack(side = TOP)    

    add_new_entry = Entry (
        frame2,
        width = 100,
        fg=color.labelfg,
        bg=color.entry,
        cursor="arrow",
        insertbackground=color.labelfg,
        font=(font,12,"normal"),
        
    )
    add_new_entry.pack(side =TOP,expand=True)



    text_label = Label (
        frame2,
        text = "TEXT :",
        fg=color.labelfg,
        bg=color.labelbg,
        cursor="arrow",
        font=(font,12,"normal"),
    )
    text_label.pack(side = TOP)    

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
    # text.config(yscrollbar=s.set)
    text.pack(side=TOP,fill=BOTH,expand=TRUE )
    # frame2.pack(side=TOP)




    key_label1 = Label (
        frame3,
        text = "KEY :",
        fg=color.labelfg,
        bg=color.labelbg,
        cursor="arrow",
        font=(font,12,"normal"),
    )
    key_label1.pack(side = TOP)    

    key_entry1 = Entry (
        frame3,
        width = 100,
        fg=color.labelfg,
        bg=color.entry,
        cursor="arrow",
        insertbackground=color.labelfg,
        font=(font,12,"normal"),
        
    )
    key_entry1.pack(side =TOP,expand=True)

    shift_label1 = Label (
        frame3,
        text = "SHIFT :",
        fg=color.labelfg,
        bg=color.labelbg,
        cursor="arrow",
        font=(font,12,"normal"),
    )
    shift_label1.pack(side = TOP)    

    shift_entry1 = Entry (
        frame3,
        width = 100,
        fg=color.labelfg,
        bg=color.entry,
        cursor="arrow",
        insertbackground=color.labelfg,
        font=(font,12,"normal"),
        
    )
    shift_entry1.pack(side =TOP,expand=True)


    add_new_label1 = Label (
        frame3,
        text = "Name of the file to store in :",
        fg=color.labelfg,
        bg=color.labelbg,
        cursor="arrow",
        font=(font,12,"normal"),
    )
    add_new_label1.pack(side = TOP)    

    add_new_entry1 = Entry (
        frame3,
        width = 100,
        fg=color.labelfg,
        bg=color.entry,
        cursor="arrow",
        insertbackground=color.labelfg,
        font=(font,12,"normal"),
        
    )
    add_new_entry1.pack(side =TOP,expand=True)


    text_label1 = Label (
        frame3,
        text = "TEXT :",
        fg=color.labelfg,
        bg=color.labelbg,
        cursor="arrow",
        font=(font,12,"normal"),
    )
    text_label1.pack(side = TOP)    

    text1=Text (
        frame3,
        width=500,
        fg=color.labelfg,
        bg=color.entry,
        cursor="arrow",
        insertbackground=color.labelfg,
        font=(font,12,"normal"),        
    )
    
    s1=Scrollbar(frame3)
    s1.pack(side=RIGHT,fill=Y)
    # text1.config(yscrollbar=s.set)
    text1.pack(side=TOP,fill=BOTH,expand=TRUE )
    # frame3.pack(side=TOP)




    myimg= PhotoImage(file="icons8-data-encryption-100.png")
    p= myimg.subsample(2,2)

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
    p5= myimg5.subsample(2,2)
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
    p2= myimg2.subsample(2,2)
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
    p14= myimg14.subsample(2,2)
    decrypt_btn=Button(
        frame,
        command=lambda:encrypt_file(),
        bg=color.buttons,
        fg=color.labelfg,
        font= (font,12,"bold"),
        padx=5,pady=2,
        image=p14,
        compound=LEFT,
        )
    decrypt_btn.pack(side=RIGHT)
    CreateToolTip(decrypt_btn,"Decrypt File")

    myimg15= PhotoImage(file="icons8-data-protection-100.png")
    p15= myimg15.subsample(2,2)
    encrypt_btn=Button(
        frame,
        command=lambda:decrypt_file(),
        bg=color.buttons,
        fg=color.labelfg,
        font= (font,12,"bold"),
        padx=5,pady=2,
        image=p15,
        compound=LEFT,
        )
    encrypt_btn.pack(side=RIGHT)
    CreateToolTip(encrypt_btn,"Encrypt File")
   

    myimg18= PhotoImage(file="icons8-padlock-100.png")
    p18= myimg18.subsample(2,2)
    decrypt_btn_str=Button(
        frame,
        command=lambda:decrypt_string(),
        bg=color.buttons,
        fg=color.labelfg,
        font= (font,12,"bold"),
        padx=5,pady=2,
        image=p18,
        compound=LEFT,
        )
    decrypt_btn_str.pack(side=RIGHT)
    CreateToolTip(decrypt_btn_str,"Decrypt Text")

    myimg16= PhotoImage(file="icons8-password-100.png")
    p16= myimg16.subsample(2,2)
    encrypt_btn_str=Button(
        frame,
        command=lambda:encrypt_string(),
        bg=color.buttons,
        fg=color.labelfg,
        font= (font,12,"bold"),
        padx=5,pady=2,
        image=p16,
        compound=LEFT,
        )
    encrypt_btn_str.pack(side=RIGHT)
    CreateToolTip(encrypt_btn_str,"Encrypt Text")
   

    
    myimg17= PhotoImage(file="icons8-align-text-left-100.png")
    p17= myimg17.subsample(2,2)
    textarea_btn=Button(
        frame,
        command=lambda:[activateText()],
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
    p11= myimg11.subsample(2,2)
    Open_btn=Button(
        frame,
        command=lambda:open_file(),
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
    p8= myimg8.subsample(2,2)
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
    
    
    


    menubar=Menu(root)
    filemenu = Menu(menubar, tearoff=0,bg=color.labelbg,fg= color.labelfg,relief=RAISED,font=(font,12,"normal"))
    menubar.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="Open Text Area",command=activateText)
    filemenu.add_command(label="Encrypt Text",command=encrypt_string)
    filemenu.add_command(label="Decrypt Text",command=decrypt_string)
    filemenu.add_separator()
    filemenu.add_command(label="Open File",command=open_file)
    filemenu.add_command(label="Encrypt File",command=encrypt_file)
    filemenu.add_command(label="Decrypt File",command=decrypt_file)
    filemenu.add_separator()





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














