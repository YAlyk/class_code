# тернарная операция, map, json.

# a = 10
# b = 5
# if a > b:
#     c = a
# else:
#     c = b
# print(c)

# #  <значение> if (условние) else <значение>
# c = a if a > b else b

# print(c)

def pw(a):
    return a**2


a = [1, 5, 9, 6, 8]
print(list(map(float, a)))


a = [1, 5, 9, 6, 8]
print(list(map(lambda x: x**2, a)))


# old_list = [1, 5, 9, 6, 8]
# new_list = []
# for item in old_list:
#     new_list.append(pw(item))
# print(new_list)
