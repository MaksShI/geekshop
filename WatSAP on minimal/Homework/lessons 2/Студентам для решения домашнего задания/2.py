import json


# {"orders": []}
def write_order_to_json():
    with open('orders.json', 'r', encoding='utf-8') as f_out:
        data = json.load(f_out)

    with open('orders.json', 'w', encoding='utf-8') as file:
        orders_list = data['orders']
        item = input('Item: ')
        quantity = int(input('quantity: '))
        price = input('price: ')
        buyer = input('buyer: ')
        dated = input('dated: ')
        mass = {'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'dated': dated}

        orders_list.append(mass)
        json.dump(data, file, indent=4, ensure_ascii=False)


#    with open('order.jsonlines', 'a', encoding='utf-8') as file:
#        json.dump(mass, file)
#        file.write('\n')


write_order_to_json()
