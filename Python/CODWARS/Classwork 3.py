def allin(s):
    s = (s + 1) // 7
    n = 36
    while s < 2050:
        s = s * 2
        n = n + 3
    return n


s = 6
count = 0
while True:
    s += 1
    if allin(s) == 60:
        break
    count += 1
print(allin(62))
#Ответ 62