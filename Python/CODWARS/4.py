def feast(beast, dish):
    beast = list(beast)
    dish = list(dish)
    if beast[0] == dish[0] and beast[len(beast)-1] == dish[len(dish)-1]:
        return True
    return False

# feast = lambda b, d: (b[0], b[-1]) == (d[0], d[-1])