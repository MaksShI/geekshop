def hex_numb(a):
    count = 0
    while a > 0:
        if a % 7 == 6:
            count += 1
        a = a // 10
    return count


print(hex_numb(7 ** 20 - 7 ** 11))
