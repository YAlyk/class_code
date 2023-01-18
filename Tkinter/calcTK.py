from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math
import sys

root = Tk() 
root.title("Calculator")

calc_entry = Entry(root, width = 33)
calc_entry.grid(row=0, column=0, columnspan=5)

#логика калькулятора
def calc(key):
    global memory
    if key == "=":
#исключение написания слов
        str1 = "-+0123456789.*/)(" 
        if calc_entry.get()[0] not in str1:
            calc_entry.insert(END, "First symbol is not number!")
            messagebox.showerror("Error!", "You did not enter the number!")
#исчисления
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, "=" + str(result))
        except:
            calc_entry.insert(END, "Error!")
            messagebox.showerror("Error!", "Check the correctness of data")
    elif key == "C":
        calc_entry.delete(0, END)
    elif key == "±":
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass
    elif key == "π":
        calc_entry.insert(END, math.pi)
    elif key == "Exit":
        root.after(1,root.destroy)
        sys.exit
    elif key == "xⁿ":
        calc_entry.insert(END, "**")
    elif key == "sin":
        calc_entry.insert(END, "=" + str(math.sin(int(calc_entry.get()))))
    elif key == "cos":
        calc_entry.insert(END, "=" + str(math.cos(int(calc_entry.get()))))
    elif key == "(":
        calc_entry.insert(END, "(")
    elif key == ")":
        calc_entry.insert(END, ")")
    elif key == "n!":
        calc_entry.insert(END, "=" + str(math.factorial(int(calc_entry.get()))))
    elif key == "√2":
        calc_entry.insert(END, "=" + str(math.sqrt(int(calc_entry.get()))))
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)

# список кнопок
bttn_list = [
"7", "8", "9", "+", "*", 
"4", "5", "6", "-", "/",
"1", "2", "3",  "=", "xⁿ",
"0", ".", "±",  "C",
"Exit", "π", "sin", "cos",
"(", ")","n!","√2", ]

r = 1
c = 0
for i in bttn_list:
    rel = ""
    cmd=lambda x=i: calc(x)
    ttk.Button(root, text=i, command = cmd, width = 10).grid(row=r, column = c)
    c += 1
    if c > 4:
        c = 0
        r += 1

root.mainloop()