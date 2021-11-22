import random

a = list(random.sample(range(20), 8))
b = list(random.sample(range(20), 8))
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
# b = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711]
print(a, b)
s = []
for x in list(a):
    for i in list(b):
        if x == i:
            s.append(x)
print(s)
