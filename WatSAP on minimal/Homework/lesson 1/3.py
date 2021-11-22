# Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
mass = ['attribute', 'класс', 'функция', 'type']
for el in mass:
    try:
        print(bytes(el, 'ascii'))
    except UnicodeEncodeError:
        print(f'Слово "{el}" невозможно записать в виде байтовом типе!')

