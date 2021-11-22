def product_array(numbers):
    mass = []
    if len(numbers) < 3:
        return numbers[::-1]
    while True:
        for i in numbers:
            k = numbers[0]
            numbers.pop(0)
            for s in range(len(numbers) + 1):
                print(i)
                print(s)
                print(k)
                if s == len(numbers):
                    pass
                else:
                    s = numbers[s + 1] * numbers[s]
            mass.append(k)
        return mass


print(product_array([3, 27, 4, 2]))  # [216,24,162,324])
