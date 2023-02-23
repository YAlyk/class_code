# a = []
# a.append()

# a = [1, 9, 6, 5, 7, 8, 1, 2, 5, 6]
# print(sum(a)/len(a))
import random
import statistics

random.seed(100)
n = 1000
d = [random.randint(0, 30) for i in range(n)]
d1 = d
print('среднее значение', sum(d)/len(d))
print('среднее значение', statistics.mean(d))


index = n // 2
if n % 2:
    ch = sorted(d1)[index]
else:
    ch = sum(sorted(d1)[index - 1:index+1])/2

print('медиана:', ch)
print('медиана:', statistics.median(d))


print('Мода:',statistics.mode(d))