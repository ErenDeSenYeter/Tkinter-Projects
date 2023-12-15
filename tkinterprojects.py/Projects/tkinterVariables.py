import tkinter as tk
from tkinter import ttk

def button_func():
    print(string_var.get())
    string_var.set("button pressed")

# window 
window = tk.Tk()
window.title("Tkinter Variables")
window.geometry("300x300")

#tkinter variable
string_var = tk.StringVar() # value="start value" // puts a string in to entry

# widgets 
label = ttk.Label(master = window, text = string_var, textvariable = string_var)
label.pack()

entry =ttk.Entry(master = window, textvariable = string_var)
entry.pack()


entry2 =ttk.Entry(master = window, textvariable = string_var)
entry2.pack()

# button
button = ttk.Button(master=window, text="Button",command=button_func)
button.pack()

# run
window.mainloop()
