import yaml

action_list = ['computer',
               'printer',
               'keyboard',
               'mouse']

to_list = {'computer': '200\u20ac',
           'printer': '300\u20ac',
           'keyboard': '150\u20ac',
           'mouse': '360\u20ac'}

data_to_yaml = {'items': action_list, 'items_price': to_list, 'items_quantity': 4}

with open('data_write.yaml', 'w', encoding='utf-8') as f_n:
    yaml.dump(data_to_yaml, f_n, allow_unicode=True, sort_keys=False)

with open('data_write.yaml', 'r', encoding='utf-8') as f_n:
    print(f_n.read())
