def reverse_words(text):
    mass = []
    klon = 0
    count = text
    text = text.split()
    for i in text:
        mass.append(i[::-1])
    print(count)
    for x in count:
        print(x)
        print(klon)
        if count[klon] == ' ' and count[int(klon) + 1] == ' ':
            mass.insert(klon, ' ')
        klon += 1

    return ' '.join(mass)


print(reverse_words('double  spaced  words'))