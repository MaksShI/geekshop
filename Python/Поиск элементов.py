def found(num, mass):
    if num in mass:
        return print(True)
    return print(False)


found(int(input("Введите число :")), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 22, 58, ])
