# 2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
# Написать скрипт, автоматизирующий его заполнение данными. Для этого:

import json
def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json', 'r', encoding='utf-8') as f_out:
        data = json.load(f_out)

    with open('orders.json', 'w', encoding='utf-8') as file:
        dict_list = {'item': item,
                     'quantity': quantity,
                     'price': price,
                     'buyer': buyer,
                     'date': date}
        order_list = data["orders"]
        order_list.append(dict_list)

#
write_order_to_json('msg', 'sng', '100', 'Petrov.A.A', '26.05.2022')

