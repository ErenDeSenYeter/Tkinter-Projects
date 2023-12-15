# There are 3 major button 
# Button, Check Button, Radio Button

import tkinter as tk
from tkinter import ttk

#setup
window = tk.Tk()
window.title("Buttons")
window.geometry("300x300")

# button
# first argument always going to be the " master = "
def button_func():
    print("It is alive")

button_string = tk.StringVar(value = "A Button with Sting Var")
button = ttk.Button(window, text = "Classic Button",command = button_func, textvariable = button_string)
# button = ttk.Button(window, text="Classic Button",command = lambda: print("a basic button"))
button.pack()

#check Button
check_var = tk.IntVar() # StringVar, IntVar and BooleanVar // Inside the IntVar can be modified as value = 10 that makes the box began on True  

check1 = ttk.Checkbutton(
                        window,
                        text="Check Box 1",
                        command= lambda: print(check_var.get()),
                        variable= check_var,
                        onvalue = 10,
                        offvalue = 5 
                        )
check1.pack()

check_variable = tk.StringVar()

check2 = ttk.Checkbutton(window,
                        text="Check Box 2",
                        command= lambda: print(check_variable.get()),
                        variable=check_variable,
                        onvalue="Acik",
                        offvalue="Kapali"
                        )
check2.pack()

# Radio Button
radio_Var = tk.StringVar()

radio1 = ttk.Radiobutton(window,text="Radio Button 1",
                          value = "radio 1",
                          variable= radio_Var,
                          command = lambda: print(radio_Var.get()))
radio1.pack()

radio2 = ttk.Radiobutton(window,text="Radio Button 2",
                        value = 2,
                        variable=radio_Var,
                        command=lambda: print(radio_Var.get()))
radio2.pack()


# exercise radios

def radio_func():
    print(check_bool.get())
    check_bool.set(False)

#data
radio_string = tk.StringVar()
check_bool = tk.BooleanVar()

#widgets
exercise_radio1 = ttk.Radiobutton(window, text = "Radio A", value= "A", command= radio_func, variable = radio_string )
exercise_radio2 = ttk.Radiobutton(window, text = "Radio B", value= "B", command= radio_func, variable = radio_string )
exercise_Check = ttk.Checkbutton(window,text="exercise check", variable= check_bool)

exercise_radio1.pack()
exercise_radio2.pack()
exercise_Check.pack()

#run
window.mainloop()

