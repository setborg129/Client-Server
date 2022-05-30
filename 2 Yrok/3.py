import yaml

data_into = {'keys':['Apply', 'Orange'],
             'item_count': 2,
             'items_price': {'Apply': '150',
                             'Orange': '53',
                            }
             }


with open('test.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(data_into, f)


with open('test.yaml', 'r', encoding='utf-8') as f_o:
    data_read = yaml.load(f_o, Loader=yaml.SafeLoader)

print(data_into)
print(data_read)

print(data_into == data_read)