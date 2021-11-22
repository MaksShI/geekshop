def maxin3(a, x, y):
    if a > x and a > y:
        return a
    elif x > a and x > y:
        return x
    elif y > a and y > x:
        return y
    else:
        return a


print(maxin3(7, 7, 7))
