x = int(input())
D = int(input())
mass = []
for i in range(0, x):
    s = int(input())
    mass.append(s)
k = 0
for i in mass:
    k += 1
    if i < D:
        break
print(k + 1)