from tkinter import *

colors=['#7FFFD4','white', 'gray', 'brown', 'yellow', 'blue', 'red','green', 'pink', 'magenta', 'black'] # список 
#  список цветов чтобы менять их на хослте 

def get_next(item): # выбор цвета послоедовательно 
    curr = colors.index(canvas.itemcget(item, 'fill'))
    print(curr)
    if curr != len(colors) - 1:
        return curr + 1
    return 0


window=Tk()
window.geometry('500x700')

def one():# стекло
    canvas.itemconfig(glass,fill=colors[get_next(glass)])
    pass
def two():# каркас
    canvas.itemconfig(polygon,fill=colors[get_next(polygon)])
    pass
def three():# колеса
    canvas.itemconfig(left_1,fill=colors[get_next(left_1)])
    canvas.itemconfig(right_2,fill=colors[get_next(right_2)])
    pass



Button(text='1', width=30,height=2,bg='black',fg='white',command=one).pack()
Button(text='2', width=30,height=2,bg='black',fg='white', command=two).pack()
Button(text='3', width=30,height=2,bg='black',fg='white',command=three).pack()



canvas=Canvas(window, height=500, width=500)
canvas.pack()

points=[115,410,215,410,
        215,355,310,355,
        310,410,405,411,
        405,475,370,475,
        370,450,305,450,
        305,475,215,475,
        215,450,150,450,
        150,475,115,475,
        ] # координаты каркаса машины 

polygon=canvas.create_polygon(points,outline='black',fill='white',width=2)

# два колеса 
left_1=canvas.create_oval(151,495,214,450,outline='black',fill='white')# левое колесо
right_2=canvas.create_oval(306,495,369,450,outline='black' ,fill='white') # правое колесо

# стекло 
glass=canvas.create_rectangle(230,405,265,365, outline='black', fill='white')

window.mainloop()










