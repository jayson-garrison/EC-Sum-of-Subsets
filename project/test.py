import random as rand
import numpy as np
print('hello!')

l = [1,2,3]
w = [.9,.05,.05]
for i in range(5):
    print(rand.choices(l, weights=w), end="")

print(np.zeros(0).size) #is 0