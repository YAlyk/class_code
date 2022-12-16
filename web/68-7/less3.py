data = [2, 3, 4, 5, 4, 5]
sum_marks = 0
i = 0
while i < len(data):
    sum_marks += data[i]
    i+=1
mean = sum_marks / len(data)
print(mean)