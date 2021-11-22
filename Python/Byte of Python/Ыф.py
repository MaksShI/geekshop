def func(N, K):
    if N == K:
        return 0
    if K == 1:
        return (N ** 2) / (K ** 2)
    return (N ** 2) / (K ** 2)


N = int(input('Input N: '))
K = int(input('Input K: '))
print(int(func(N, K)))