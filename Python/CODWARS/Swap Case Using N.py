def swap(s, n):
    s.split()
    mass = []
    array = '''! @ # $ % ^ & * ( ) _ - = + [ } ] { " : ; ' > < , .  '''
    array.split(' ')
    print(array)
    k = 0
    a = 0
    n = str(bin(n))
    n = list(n)
    n.pop(0)
    n.pop(0)
    for i in s:
        print(a)
        print(n)
        print(mass)
        if len(n) == a:
            a = 0
        else:
            pass
        if s[k] in array:
            a = a - 1
            mass.append(s[k])
        elif n[a] == '1':
            if s[k].upper() == s[k]:
                mass.append(s[k].lower())
            else:
                mass.append(s[k].upper())
        else:
            mass.append(s[k])
        k += 1
        a += 1
    return ''.join(mass)


print(swap('tvFhWIvAKPkS?d"vz?.wGn"', 345004)) # tvFhWIvAKPkS?D"vZ?.wgN"
