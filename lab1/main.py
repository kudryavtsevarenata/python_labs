import random
from statistics import median
sum = 0
mx_num = 888888
n = mx_num + 1
for i in range(0, mx_num+1):
    sum += i
print("Сумма ряда =", sum)
print("Среднее этого ряда =", int(sum/n))

a = random.sample(range(0, mx_num), 100)
sm = 0
for i in range(0, len(a)):
    sm += a[i]
print("Сумма 100 случайных чисел из промежутка =", sm)
print("Медиана =", median(a))



