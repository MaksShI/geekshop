def more_inf():
    return 'sasda'


fileling = str(input('Введите название файла: ')) + '.txt'
with open(fileling, 'w') as open_file:
    open_file.write(more_inf())
