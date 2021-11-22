def disarium_number(number):
    k = 0
    s = 0
    for i in str(number):
        k += 1
        s += int(i) ** k
    if s == number:
        return "Disarium !!"
    return "Not !!"


print(disarium_number(518))
