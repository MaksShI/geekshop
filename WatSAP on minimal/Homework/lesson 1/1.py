# Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание соответствующих переменных.
# Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode и также проверить тип и содержимое переменных.
mass = ['разработка', 'сокет', 'декоратор']
print('разработка', 'сокет', 'декоратор')
print(type(mass[0]))
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
all_in = '\u0430\u0431\u0432\u0433\u0434\u0435\u0451\u0436\u0437\u0438\u0439\u043a\u043b\u043c\u043d\u043e\u043f\u0440\u0441\u0442\u0443\u0444\u0445\u0446\u0447\u0448\u0449\u044a\u044b\u044c\u044d\u044e\u044f'
sum_words = ''
for k in mass:
    k += ' '
    for x in k:
        s = 0
        while True:
            if x == ' ':
                sum_words += ' '
                break
            if x == alphabet[s]:
                sum_words += all_in[s]
                break
            s += 1
print(sum_words)
print(type(sum_words))