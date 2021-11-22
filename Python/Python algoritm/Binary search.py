def binary_search(list, item):
    low = 0
    hight = len(list) - 1

    while low <= hight:
        mid = (low + hight) // 2
        print(mid)
        guess = list[mid]
        print(guess)
        if guess == item:
            return mid
        elif guess > item:
            hight = mid - 1
        else:
            low = mid + 1
    return None


# my_list = [int(n) for n in range(0, 10, 3)]
my_list = [8, 9, 2, 4, 1, 4, 2]
print(my_list)
print(binary_search(my_list, 1))
