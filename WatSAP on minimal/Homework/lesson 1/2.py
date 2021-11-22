# Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
# (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
all_words = 'class function method'
print(all_words)  # объект
print(type(all_words))  # тип
print(len(all_words))  # длинна
sum_array = []
bait_words = b'class function method'
for i in bait_words:
    sum_array.append(i)

print(sum_array)  # объект
print(type(bait_words))  # тип
print(len(bait_words))  # длинна
