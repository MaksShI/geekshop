def minimum_steps(numbers, value):
    array = []
    k = 0
    s = 0
    x = 0
    while s <= value:
        if len(numbers) < 2:
            return x
        k = min(numbers)
        if k > value:
            return 0
        if k in array:
            l = 0
            p = 0
            for i in numbers:
                l += 1
                if i == k and p == 0:
                    numbers.pop(l - 1)
                    p += 1
        else:
            array.append(k)
            s = sum(array)
            x += 1
            if s >= value:
                return x - 1
    return x - 1


print(minimum_steps([19, 98, 69, 28, 75, 45, 17, 98, 67], 464))  # 8
