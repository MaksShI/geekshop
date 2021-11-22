import csv
import re


def get_data():
    os_name_list = []
    os_code_list = []
    os_prod_list = []
    os_type_list = []
    main_data = []

    for i in range(1, 4):
        file_obj = open(f'info_{i}.txt')
        data = file_obj.read()

        os_prod_reg = re.compile(r'Изготовитель системы:\s*\S*')
        os_prod_list.append(os_prod_reg.findall(data)[0].split()[2])

        os_name_reg = re.compile(r'Windows\s*\S*')
        os_name_list.append(os_name_reg.findall(data)[0])

        os_code_reg = re.compile(r'Код продукта:\s*\S*')
        os_code_list.append(os_code_reg.findall(data)[0].split()[2])

        os_type_reg = re.compile(r'Тип системы:\s*\S*')
        os_type_list.append(os_type_reg.findall(data)[0].split()[2])

    headers = ['Номер', 'Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    main_data.append(headers)

    j = 0
    for i in range(0, 3):
        row_data = []
        row_data.append(j)
        row_data.append(os_prod_list[i])
        row_data.append(os_name_list[i])
        row_data.append(os_code_list[i])
        row_data.append(os_type_list[i])
        main_data.append(row_data)
        j += 1
    return main_data


def writer_csv(out):
    main_data = get_data()
    with open('log_file.csv', 'w', encoding='utf-8', newline='') as f_n:
        f_n_writer = csv.writer(f_n, quoting=csv.QUOTE_NONNUMERIC)
        for i in main_data:
            f_n_writer.writerow(i)


writer_csv('log_file.csv')
