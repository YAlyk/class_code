
# root = Tk()
# root.title('Первое приложение на Tkinter')
# root.geometry('700x500')
# Label(text='Это текст').pack
# Entry(text='Поле для ввода').pack
# Button(text='Это кнопка').pack

# l1 = Label(text='Это текст 1')
# l2 = Label(text='Это текст 2')
# l3 = Label(text='Это текст 3')
# l4 = Label(text='Это текст 4')

# l1.pack(side=BOTTOM)
# l2.pack(side=BOTTOM)
# l3.pack(side=BOTTOM)
# l4.pack(side=BOTTOM)

# bt = Button(width=50, height=20, bg='cyan', activebackground='red', text="это кнопка!")
# bt.pack()


# bt1 = Button(width=10, height=20, bg='blue', activebackground='grey')
# bt2 = Button(width=10, height=20, bg='orange', activebackground='black')
# bt3 = Button(width=10, height=20, bg='yellow', activebackground='red')
# bt4 = Button(width=10, height=20, bg='white', activebackground='pink')
# bt1.pack(side=TOP)
# bt2.pack(side=BOTTOM)
# bt3.pack(side=RIGHT)
# bt4.pack(side=LEFT)


# ent = Entry(root, width=20, bg='black', fg='white')
# ent.pack()


# преобразование текста
# def str_to_sort_list():
#     s = ent.get()
#     s = s.split()
#     s.sort()
#     lab['text'] = ' '.join(s)

# ent = Entry(width=20)
# but = Button(text="Преобразовать", command=str_to_sort_list)
# lab = Label(width=20, bg='black', fg='white')

# # but.bind('<Button-1>', str_to_sort_list)

# ent.pack()
# but.pack()
# lab.pack()


# root.mainloop()


# from tkinter import *
# root = Tk()
# canvas = Canvas(root, width=500, height=500, bg='white')
# canvas.pack()
# canvas.create_line(10, 10, 150, 150) # координаты точек, x1 y1 x2 y2
# root.mainloop()


# from tkinter import *
# root = Tk()
# canvas = Canvas(root, width=500, height=500, bg='white')
# canvas.pack()
# canvas.create_rectangle(5, 5, 100, 125, fill='yellow', activeoutline='red', dash=(30, 20, 10), width=5)
# root.mainloop()
# from tkinter import *


# def change():
#     canvas.itemconfig(square, fill='blue')
#     print(canvas.itemcget(square, 'fill'))


# side = 200
# canvas_width, canvas_height = 300, 300
# x, y = 20, 20
# root = Tk()
# canvas = Canvas(root, width=canvas_width, height=canvas_height, bg='white')
# canvas.pack()
# square = canvas.create_rectangle(x, y, x+side, y+side, fill='yellow')
# Button(text='1244', command=change).pack()
# root.mainloop()


# from tkinter import *
# colors = ['#7FFFD4', 'white', 'gray', 'brown', 'yellow',
#           'blue', 'red', 'green', 'pink', 'magenta', 'black']


# def get_next(item):
#     curr = colors.index(canvas.itemcget(item, 'fill'))
#     if curr != len(colors) - 1:
#         return curr + 1
#     return 0


# def change_square():
#     canvas.itemconfig(square, fill=colors[get_next(square)])


# def change_roof():
#     canvas.itemconfig(roof, fill=colors[get_next(roof)])


# def change_sun():
#     canvas.itemconfig(sun, fill=colors[get_next(sun)])


# side = 200
# canvas_width, canvas_height = 500, 500
# x, y = 150, 300
# root = Tk()
# canvas = Canvas(root, width=canvas_width, height=canvas_height, bg='white')
# canvas.pack()
# square = canvas.create_rectangle(
#     x, y, x+side, y+side, fill=colors[2], outline='white')
# roof = canvas.create_polygon(
#     x, y, x+side, y, x+side//2, y-side//2, fill=colors[1], outline='white')
# sun = canvas.create_oval(canvas_width - side//2, 0,
#                          canvas_width, side//2, fill=colors[3], outline='white')
# Button(text='Основание', command=change_square).pack()
# Button(text='Крыша', command=change_roof).pack()
# Button(text='Солнце', command=change_sun).pack()
# root.mainloop()


from tkinter import *
def change():
    canvas.itemconfig(square, fill='black') 
def change():   
    canvas.itemconfig(sun, fill='black')
def change():    
    canvas.itemconfig(osnovanie, fill='black')

canvas_width, canvas_height = 300, 300
x, y=20, 20
root=Tk()

canvas=Canvas(root, width=canvas_width, height=canvas_height, bg='white')
canvas.pack() 

square=canvas.create_rectangle(150, 150, 200, 200, fill="yellow") 
sun=canvas.create_oval(250, 50, 300, 100, fill='yellow')
osnovanie=canvas.create_polygon(150, 150, 175, 125, 200, 150, fill='grey')

Button(text='Основание', command=change).pack() 
Button(text='Крыша', command=change).pack() 
Button(text='Солнце', command=change).pack() 

root.mainloop()