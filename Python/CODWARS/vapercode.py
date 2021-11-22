def vaporcode(s):
    s = list(s)
    i = 0
    while i != len(s)-1:
        if s[i] == " ":
            s.pop(i)
        i += 1
    s = '  '.join(s)
    s = s.upper()
    return s


print(vaporcode("g xMemt!wnWwdeclETWB! T'uPXZiJaIRsguVJyjBc "))
