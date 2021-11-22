def jumping_number(number):
    s = 0
    number = str(number)
    for i in number:
        i = int(i)
        s += 1
        if s < len(number):
            k = number[s]
            k = int(k)
        else:
            return "Jumping!!"
        if i + 1 == k or i - 1 == k:
            pass
        else:
            return "Not!!"
    return "Jumping!!"


print(jumping_number(789))
