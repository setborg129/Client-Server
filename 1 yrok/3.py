# Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
# Важно: решение должно быть универсальным, т.е. не зависеть от того, какие конкретно слова мы исследуем.


# word_num1 = b'attribute'
# print(type(word_num1))
# word_num2 = b'класс'       # Не может записать в байтовый тип.
# print(type(word_num2))
# word_num3 = b'функция'
# print(type(word_num3))
# word_num4 = b'type'


str_1 = 'attribute'
str_2 = 'класс'
str_3 = 'функция'
str_4 = 'type'

Words_list = [str_1, str_2, str_3, str_4]


for item_list in Words_list:
    try:
     item_list.encode('ascii')
    except UnicodeEncodeError:
        print(f'{item_list}, не возможно записать в байтовый тип')