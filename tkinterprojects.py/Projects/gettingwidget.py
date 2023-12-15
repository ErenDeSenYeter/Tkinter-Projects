import tkinter as tk
from tkinter import ttk


def button_function():
    # get the content of the entry
    entry_text = Entry.get()

    # update the label
    # Label.configure(text="some other text")
    # or
    Label["text"] = entry_text
    
    # print(Label.configure())
    # infos about what can we do in Label

    # after one entry it closes the widget
    Entry["state"] = "disabled"

def fix_it():
    entry_text2 = "This is an another text"
    Label["text"]=entry_text2
    Entry["state"]= "enabled"

# window
window = tk.Tk()
window.title("Getting and Setting WIDGETS")
window.geometry("300x200")

# widgets
Label =  ttk.Label(master=window, text= "This is a test ")
Label.pack()

Entry = ttk.Entry(master=window)
Entry.pack()

Button = ttk.Button(master=window,text="press me", command= button_function)
Button.pack()

Button2 = ttk.Button(master=window, text = "fix it ?", command=fix_it)
Button2.pack()
# run
window.mainloop()
