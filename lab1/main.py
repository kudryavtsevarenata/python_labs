import random
from statistics import median
mx_num = 888888
n = mx_num + 1
sm = sum([x for x in range(0, n)])
print("Summ =", sm)
print("Average =", int(sm/n))

a = random.sample(range(0, mx_num), 100)
sm = 0
for i in range(0, len(a)):
    sm += a[i]
print("Summ of 100 random integers =", sm)
print("Median =", median(a))



