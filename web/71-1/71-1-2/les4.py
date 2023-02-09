# from tkinter import *
# from tkinter import ttk
# from tkinter.messagebox import showerror, showwarning, showinfo

# root = Tk()
# root.title("test")
# root.geometry("250x200")


# def open_info():
#     showinfo(title="Информация", message="Информационное сообщение")


# def open_warning():
#     showwarning(title="Предупреждение", message="Сообщение о предупреждении")


# def open_error():
#     showerror(title="Ошибка", message="Сообщение об ошибке")


# info_button = ttk.Button(text="Информация", command=open_info)
# info_button.pack(anchor="center", expand=1)

# warning_button = ttk.Button(text="Предупреждение", command=open_warning)
# warning_button.pack(anchor="center", expand=1)

# error_button = ttk.Button(text="Ошибка", command=open_error)
# error_button.pack(anchor="center", expand=1)

# root.mainloop()


# from tkinter import *
# from tkinter import ttk
# from tkinter.messagebox import showinfo, askyesno

# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x200")

# def click():
#     result = askyesno(title="Подтвержение операции", message="Подтвердить операцию?")
#     if result: showinfo("Результат", "Операция подтверждена")
#     else: showinfo("Результат", "Операция отменена")

# ttk.Button(text="Click", command=click).pack(anchor="center", expand=1)

# root.mainloop()


# from tkinter import *
# from tkinter import ttk
# from tkinter.messagebox import showinfo, askyesnocancel

# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x200")


# def click():
#     result = askyesnocancel(title="Подтвержение операции",
#                             message="Подтвердить операцию?")
#     if result == None:
#         showinfo("Результат", "Операция приостановлена")
#     elif result:
#         showinfo("Результат", "Операция подтверждена")
#     else:
#         showinfo("Результат", "Операция отменена")


# ttk.Button(text="Click", command=click).pack(anchor="center", expand=1)

# root.mainloop()


# from tkinter import *
# from tkinter import ttk
# from tkinter.messagebox import OK, INFO, showinfo

# root = Tk()
# root.title('Название окна')
# root.geometry('250x200')


# def click():
#     showinfo(title='Название', message='текст для теста',
#              detail='text', icon=INFO, default=OK)


# ttk.Button(text='click', command=click).pack(anchor='center', expand=1)

# root.mainloop()


# from tkinter import *
# from tkinter import ttk
# root = Tk()
# root.title('название')
# root.geometry('200x200')

# btn = ttk.Button(text='click me')
# btn.place(relx=.5, rely=.5, anchor='center', width=80, height=80)

# root.mainloop()


# from tkinter import *
# from tkinter import ttk
# root = Tk()
# root.title('название')
# root.geometry('250x200')

# for c in range(4):
#     root.columnconfigure(index=c, weight=1)
# for r in range(4):
#     root.rowconfigure(index=r, weight=1)

# for r in range(4):
#     for c in range(4):
#         btn = ttk.Button(text=f'({r}, {c})')
#         btn.grid(row=r, column=c, ipadx=6, ipady=6, padx=[15,4], pady=4)
# root.mainloop()


# from tkinter import *
# from tkinter import ttk
# root = Tk()
# root.title('название')
# root.geometry('250x200')

# for c in range(2):
#     root.columnconfigure(index=c, weight=1)
# for r in range(2):
#     root.rowconfigure(index=r, weight=1)

# btn1 = ttk.Button(text='button1')
# btn1.grid(row=0, column=0, columnspan=2, ipadx=70, ipady=6, padx=5, pady=5)

# btn3 = ttk.Button(text="button 3")
# btn3.grid(row=1, column=0, ipadx=6, ipady=6, padx=5, pady=5)

# btn4 = ttk.Button(text="button 4")
# btn4.grid(row=1, column=1, ipadx=6,  ipady=6, padx=5, pady=5)
# root.mainloop()


# from tkinter import *
# from tkinter import ttk
# root = Tk()
# root.title('название')
# root.geometry('250x200')

# for c in range(2):
#     root.columnconfigure(index=c, weight=1)
# for r in range(2):
#     root.rowconfigure(index=r, weight=1)

# btn2 = ttk.Button(text='button1')
# btn2.grid(row=0, column=1, rowspan=2, ipadx=6, ipady=55, padx=5, pady=5)

# btn1 = ttk.Button(text="button 3")
# btn1.grid(row=0, column=0, ipadx=6, ipady=6, padx=5, pady=5)

# btn3 = ttk.Button(text="button 4")
# btn3.grid(row=1, column=0, ipadx=6,  ipady=6, padx=5, pady=5)
# root.mainloop()


# from tkinter import *
# from tkinter import ttk

# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x200")

# for c in range(3):
#     root.columnconfigure(index=c, weight=1)
# for r in range(3):
#     root.rowconfigure(index=r, weight=1)

# for r in range(3):
#     for c in range(3):
#         btn = ttk.Button(text=f"({r},{c})")
#         btn.grid(row=r, column=c, ipadx=6, ipady=6,
#                  padx=4, pady=4, sticky=NSEW)

# root.mainloop()
