from tkinter import *
from tkinter import messagebox as mb

from tkinter import filedialog as fd

font="Times New Roman"

global key, text, address, shift

label_color = "#f2f2f2"
button_color = "#ffffcc"
bg_color = "#f2f2f2"
fg_color = "black"

def main():
    root= Tk()

    root.title("Encryption System")

    frame1 = Frame(root)

    text_entry = Text(
        frame1,
        width=500,
        fg=fg_color,
        bg=bg_color,
        cursor="arrow",
        font=(font,12,"normal"),        

    )
    text_entry.pack(side =TOP,expand=True)
    key_entry = Entry (
        frame1,
        width = 100,
        fg=fg_color,
        bg=bg_color,
        cursor="arrow",
        font=(font,12,"normal"),
        
    )
    key_entry.pack(side =TOP,fill=X)

    shift_entry = Entry (
        frame1,
        width = 100,
        fg=fg_color,
        bg=bg_color,
        cursor="arrow",
        font=(font,12,"normal"),
        
    )
    shift_entry.pack(side =TOP,fill=X)

    
    s=Scrollbar(frame1)
    s.pack(side=RIGHT,fill=Y)
    # text.config(yscrollbar=s.set)
    text_entry.pack(side=TOP,fill=BOTH,expand=TRUE )

    frame1.pack()
    



    root.mainloop()

main()