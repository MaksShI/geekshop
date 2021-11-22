s = [98, 2, 10, 100, 15, 1, 23]
l = len(s)
mass = []
while True:
    x = max(s)
    k = 0
    for i in s:
        if i < x:
            x = i
    for i in s:
        k += 1
        if x == i:
            s.pop(k - 1)
    mass.append(x)
    if len(mass) >= l:
        print(mass)
        break

