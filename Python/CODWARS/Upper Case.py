def int_diff(lst, n):
    l = 0
    for i in lst:
        del lst[0]
        for x in lst:
            print(i)
            print(x)
            if i - x == n:
                l += 1
            elif x - i == n:
                l += 1
    return l


print(int_diff([1, 1, 5, 6, 9, 16, 27], 4))
