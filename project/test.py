import random as rand
import numpy as np
print('hello!')

l = [1,2,3]
w = [.9,.05,.05]
for i in range(5):
    print(rand.choices(l, weights=w), end="")

print(np.zeros(0).size) #is 0

print(l.index(1))

for idx, item in enumerate(l):
    l[idx] = item + 1

print(l)

n = np.array([1,2,3,4,5])
print(n)
print(n[3:])