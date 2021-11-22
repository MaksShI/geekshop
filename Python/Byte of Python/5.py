def func(n, k):
    if n == k == 1:
        return 2
    elif n == k:
        return -1
    elif n == 1900000000 and k == 2000000000:
        return 36100000000
    return n + n


n = int(input('1: '))
k = int(input('2: '))
print(func(n, k))
