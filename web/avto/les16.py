from tkinter import *
import tkinter as tk

window = tk.Tk()
window.title('название окна')
window.geometry('900x900')

logo = PhotoImage(file=r'web\avto\hp.png')

greeting = tk.Label(
    text='какой-то текст',
    background='black', # bg =''
    foreground='#63e028',  # fg=''
    width=20,
    height=20,
    font=('Arial', 14))
greeting.place(relx=0.5, rely=0.5,)

# label = tk.Label(image=logo,text='какой-то текст', compound='top')
# label.pack(anchor=)
window.mainloop()
