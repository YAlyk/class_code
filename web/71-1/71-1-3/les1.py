# a = int(input())
# b = int(input())
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a % b)
# print((a**10 + b**10)**0.5)


# hello = input()
# print(f"{len(hello)*60//100} р. {len(hello)*60%100} коп.")


# р - решка,   о - орёл


# s = input()
# c, i = 0, 0
# while i < len(s):
#     if s[i] == 'Р':
#         temp = 0
#         while i < len(s) and s[i] !='О':
#             temp+=1
#             i+=1
#         c=max(temp, c)
#     i+=1
# print(c)


# s=input()
# s=s.replace('ОО', 'О')
# s=s.split('О')
# m=0
# print(s)
# for i in s:
#     m=max(m, len(i))
# print(m)


from tkinter import *
colors = ['#7FFFD4', 'white', 'gray', 'brown', 'yellow',
          'blue', 'red', 'green', 'pink', 'magenta', 'black']


def get_next(item):
    curr = colors.index(canvas.itemcget(item, 'fill'))
    if curr != len(colors) - 1:
        return curr + 1
    return 0


def change_glass():
    canvas.itemconfig(glass, fill=colors[get_next(glass)])


def change_frame():
    canvas.itemconfig(frame, fill=colors[get_next(frame)])


def change_tires():
    canvas.itemconfig(tires, fill=colors[get_next(tires)])


side = 200
canvas_width, canvas_height = 500, 500
x, y = 150, 300
root = Tk()
canvas = Canvas(root, width=canvas_width, height=canvas_height, bg='white')
canvas.pack()
# glass = canvas.create_rectangle(
#     x, y, x+side, y+side, fill=colors[2], outline='white')
# frame = canvas.create_polygon(
#     x, y, x+side, y, x+side//2, y-side//2, fill=colors[1], outline='white')
tires1 = canvas.create_oval(
    160, 500, 200, 460, fill=colors[3], outline='black', width=2)
tires2 = canvas.create_oval(
    320, 500, 360, 460, fill=colors[3], outline='black', width=2)
Button(text='Стекло', command=change_glass).pack()
Button(text='Корпус', command=change_frame).pack()
Button(text='Шины', command=change_tires).pack()
root.mainloop()
