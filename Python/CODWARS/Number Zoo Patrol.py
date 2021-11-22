import random


def find_missing_number(numbers):
    if 1 not in numbers:
        return 1
    x = 0
    for i in numbers:
        if i + 1 not in numbers:
            return i + 1


mass = random.sample(range(100), 50)
print(mass)
print(find_missing_number(mass))