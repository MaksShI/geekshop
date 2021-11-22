def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


def flatten_and_sort(array):
    mass = []
    for i in array:
        for k in i:
            mass.append(k)
    return quick_sort(mass)


print(flatten_and_sort([[1, 3, 5], [100], [2, 4, 6]]))
