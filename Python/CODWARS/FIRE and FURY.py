def fire_and_fury(tweet):
    s = ''
    if 'FURY' in tweet:
        s += 'I am furious.'
    elif 'FIRE' in tweet:
        s += 'You are fired!'
    return "Fake tweet."


print((fire_and_fury("FURYYYFIREYYFIRE")))
