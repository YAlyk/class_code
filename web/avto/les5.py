# a = 'привет мир'
# print(a[0:6:1]+', '+a[-3::])
# print(a[:])
f = open('web/avto/test.txt', 'w')
f.write('test string\nperenos')
print(f.tell())
f.seek(0)
print(f.tell())
f.close()