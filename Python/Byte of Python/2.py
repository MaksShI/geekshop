X = int(input('X: '))
Y = int(input('Y: '))
N = int(input('N: '))
count = 0
k = 0
l = 0
while count != N:
    k += 1
    l += 1
    if l % 2 == 0:
        if (count + Y) <= N:
            count += Y
        else:
            l -= 1
    else:
        count += X
print(k)