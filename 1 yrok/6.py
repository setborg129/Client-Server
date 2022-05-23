
list_temple = ['сетевое программирование', 'сокет', 'декоратор']
with open('text.txt', 'w') as file:
    for num, in_write in enumerate(list_temple):
        file.write(f'{num+1}.{in_write.upper()}\n')
file.close()

# # Наполняем небольшой лист известных кодировок.
encoding = [ 'utf-8', 'cp500', 'utf-16', 'GBK', 'windows-1251', 'ASCII', 'US-ASCII', 'Big5']

for enc in encoding:
    try:
        with open('text.txt', 'r', encoding=enc) as f:
            read = f.read()
            print(f'Кодировка файла = {enc} подходит')
    except   (UnicodeDecodeError, UnicodeError):
                continue
file.close()






