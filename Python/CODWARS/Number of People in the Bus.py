def number(bus_stops):
    s = 0
    x = 0
    for k in bus_stops:
        s += k[1]
        x += k[0]
    return x - s


print((number([[10, 0], [3, 5], [5, 8]])))
