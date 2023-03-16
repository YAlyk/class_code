a = [['a','b', 'c'], ['1', '2']]
with open('input', 'w') as file:
    for i in a:
        file.write(', '.join(i)+'\n')