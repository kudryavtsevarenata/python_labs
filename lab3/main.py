from pyDatalog import pyDatalog
import random
pyDatalog.create_terms('X, Z, y, Sm, P, div, Average, N, Y, SumRand, Med, mas')
(y['sum'] == sum_(Y, for_each=Y)) <= ((Y.in_(range(1, 888888))))
print(y['sum'] == Sm)
(div[X, Y] == Z) <= (X // Y == Z)
print(div[y['sum'], 888888] == Average)
# y['random_row'] == Z.in_(random.sample(range(0, 20), 7))
# print(Z.in_(sorted(random.sample(range(0, 20), 7))))
(y['sum_rand'] == sum_(Z, for_each=Z)) <= Z.in_(random.sample(range(1, 888888), 100))
print(div[y['sum_rand'], 100] == Med)
print(y['sum_rand'] == SumRand)