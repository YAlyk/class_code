from struct import pack
from tkinter import *
# from tkinter.ttk import Combobox
# from tkinter.ttk import Checkbutton
# from tkinter.ttk import Radiobutton
# from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import ttk
from webbrowser import BackgroundBrowser
from tkinter import filedialog
from os import path
from tkinter import Menu

# def clicked():
#     messagebox.showinfo("название", "Справка о приложении:\nкакой-то текст")
#     messagebox.showwarning("название", "текст")
#   lbl.configure(text=selected.get())

window = Tk()
window.title("название приложения!")
window.geometry('800x400') #высота\ширина


tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text="первая вкладка")
tab_control.add(tab2, text="вторая вкладка")
lbl1 = Label(tab1, text='вкладка первая', padx=15, pady=15)
lbl2 = Label(tab2, text='вторая вкладка')
lbl1.grid(column=0,row=0)
lbl2.grid(column=0, row=0)
tab_control.pack(expand=1, fill="both")

# menu = Menu(window)
# new_item = Menu(menu, tearoff=0)
# new_item.add_command(label="Новый")
# new_item.add_separator()
# new_item.add_command(label="Изменить")
# new_item.add_separator()
# new_item.add_command(label="Справка", command=clicked)
# menu.add_cascade(label='Файл', menu = new_item)
# window.config(menu=menu)

# file = filedialog.askopenfilename(initialdir= path.dirname(__file__))

# file = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"),("all files","*.")))
# dir = filedialog.askdirectory()

# style = ttk.Style()
# style.theme_use('default')
# style.configure("black.Horizontal.TProgressbar", background = "black")
# bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
# bar['value'] = 50
# bar.grid(column=0, row=0)

# var = IntVar()
# var.set(36)
# spin = Spinbox(window, from_=0, to=100, width=5 ,textvariable=var)
# spin.grid(column=0, row=0)

# btn = Button(window, text="нажми меня", command=clicked)
# btn.grid(column=0, row=0)

# res = messagebox.askquestion("nazvanie", "text")

# res = messagebox.askyesno("nazvanie", "text")
# res = messagebox.askretrycancel("nazvanie", "text")
# res = messagebox.askokcancel("nazvanie", "text")
# res = messagebox.askyesnocancel("nazvanie", "text")

# txt = scrolledtext.ScrolledText(window, width =50, height = 100)
# txt.insert(INSERT, 'ТЕКСТОВОЕ ПОЛЕ')
# txt.delete(1.0, END)
# txt.grid(column=0,row=0)
# selected = IntVar()

# rad1 = Radiobutton(window, text='one_var', value=1, variable= selected)
# rad2 = Radiobutton(window, text='two_var', value=2, variable= selected)
# rad3 = Radiobutton(window, text='three_var', value=3, variable= selected)

# btn = Button(window, text="клик", command=clicked)

# lbl = Label(window)

# lbl.grid(column=0, row=1)# column - строка, row - стобец
# rad1.grid(column=0, row=0)
# rad2.grid(column=1, row=0)
# rad3.grid(column=2, row=0)
# btn.grid(column=3, row=0)

# chk_state = IntVar()
# chk_state.set(1)
# chk = Checkbutton(window, text='text', var = chk_state)
# chk.grid(column=0, row=0)

# combo = Combobox(window)
# combo['values'] = (1, 2, 3, "text")
# combo.current(0)
# combo.grid(column=0,row=0)




# btn = Button(window, text = "кнопка!", bg="black", fg="red", command=clicked)
# btn.grid(column=0, row=1)
# txt = Entry(window, width=20, state='disable')
# txt.grid(column=0, row=2)
# txt.focus()

window.mainloop()