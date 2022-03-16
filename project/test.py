import random as rand
print('hello!')

l = [1,2,3]
w = [.9,.05,.05]
for i in range(5):
    print(rand.choices(l, weights=w), end="")