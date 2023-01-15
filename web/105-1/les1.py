# a = [1,5,8,3,54,8,9,3,5,6]
# a = ['text']
# print(a)

# a = (1, 8, 9, 3, 4, 8, 58, 6, 2)
# b = a.index(9)
# print(b)


# mydict = {'Мерс': ["С класс", "В класс"], 'БМВ': ['x2', 'x3']}
# print(mydict)
# v = mydict.pop('БМВ')
# print(mydict)
# print(v)


# list = list(map(int, input().split()))
# listmax = max(list)
# listlen = len(list)
# print('#' * listmax)
# for i in list:
#     print('#'+"*" * int(i)+' '+'#')
# print('#'*max(list))


# n = list(map(int, input().split()))
# xmax = len(n)
# ymax = max(n)

# print('*'*(xmax+2))
# print('*'+' '*xmax+'*')
# for y in range(1, ymax+1):
#     print(end='*')
#     for nk in n:
#         if nk >= ymax-y+1:
#             print(end='*')
#         else:
#             print(end=' ')
#     print('*')


# a = {'apple', 'orange', 'mandarin', 'banan'}
# b = {'google', 'apple', 'microsoft'}
# # print(a ^ b)
# a.


# a = input().lower()
# print(a)
# b = input().upper()
# print(b)

alfavit = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
           'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.',
           'o': '---', 'p': '.--.', 'q': '--.-',
           'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
           'y': '-.--', 'z': '--..'}
text = input().lower().split()
a = []
for i in text:
    print(''.join(alfavit[j] for j in i))

# a = [1, 2, 3]
# for i in a:
#     print(i)