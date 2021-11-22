def number_of_rectangles(m, n):
    s = 0
    x = 0
    for i in range(1, m + 1):
        for k in range(1, n + 1):
            print(i)
            print(k)
            s += (i * k)
            print(s)
    return s


print(number_of_rectangles(120000, 1014))

# 1834 1014 = 865923260475
# 1014 1834 = 865923260475