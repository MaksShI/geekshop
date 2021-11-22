def all(seq, fun):
    print(list(seq))
    print(list(filter(fun, seq)))
    return True if list(seq) == list(filter(fun, seq)) else False


mass = [1, 2, 3, 4, 5]
f = lambda x: x < 9
print(all(mass, f))
