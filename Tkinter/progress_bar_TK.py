# from tkinter import *
# from tkinter.ttk import *
# import time

# ws = Tk()
# ws.title('название')
# ws.geometry('400x250+1000+300')


# def step():
#     for i in range(5):
#         ws.update_idletasks()
#         pb1['value'] += 20

#         time.sleep(0.5)


# pb1 = Progressbar(ws, orient=VERTICAL, length=100, mode='indeterminate')
# pb1.pack(expand=True)

# Button(ws, text='Start', command=step).pack()

# ws.mainloop()

from tkinter import *
from tkinter.ttk import Progressbar
import time


def step():
    for i in range(10):
        ws.update_idletasks()
        pb['value'] += 10
        time.sleep(1)
        txt['text']=pb['value'],'%'

ws = Tk()
ws.title('PythonGuides')
ws.geometry('800x400')
ws.config(bg='#345')


pb = Progressbar(
    ws,
    orient = HORIZONTAL,
    length = 400,
    mode = 'determinate'
    )

pb.place(x=40, y=20)

txt = Label(
    ws,
    text = '0%',
    bg = '#345',
    fg = '#fff'
)

txt.place(x= 400 ,y=200 )

Button(
    ws,
    text='Start',
    command=step
).place(x=40, y=50)

ws.mainloop()
