import tkinter as tk
from tkinter import ttk 

def button_func():
    print("a button was pressed")

def button_func2():
    print("hello")

#  create a window /root /app
window = tk.Tk()
window.title("Window and Widgets")
window.geometry("800x500")

#  tk.Text  
text = tk.Text(master = window)
text.pack()

#  ttk label 
# if we put this lines of code above the create widgets 
# it will create thee message above the test
label =  ttk.Label(master=window, text= "This is a test ")
label.pack()

label2 =  ttk.Label(master=window, text= "MY Label ")
label2.pack()

#  ttk entry
entry = ttk.Entry(master=window)
entry.pack()


#   ttk button
button = ttk.Button(master=window, text="A Button", command=button_func)
button.pack()

button2 = ttk.Button(master=window, text="2 Button", command=button_func2)
button2.pack()


#  run
window.mainloop()
