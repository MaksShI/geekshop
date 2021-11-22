def infected(s):
    all = 0
    xum_all = 0
    s = s.split('X')
    if s == None or s == 0:
        return 0
    for i in s:
        if '1' in i:
            xum_all += len(i)
        all += len(i)
    return xum_all * 100 / all

print(infected('01000000X000X011X0X'))