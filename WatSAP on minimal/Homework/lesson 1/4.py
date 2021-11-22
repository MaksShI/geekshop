# Преобразовать слова «разработка», «администрирование», «protocol», «standard»
# из строкового представления в байтовое и выполнить обратное преобразование (используя методы encode и decode).
mass = ['разработка', 'администрирование', 'protocol', 'standard']
count = 0
print(mass)
for i in mass:
    mass[count] = i.encode('utf-8')
    count += 1
print(mass)
count = 0
for i in mass:
    mass[count] = i.decode()
    count += 1
print(mass)