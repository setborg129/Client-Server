# Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
# Важно: решение должно быть универсальным, т.е. не зависеть от того, какие конкретно слова мы исследуем.
# 3
word_num1 = b'attribute'
print(type(word_num1))
word_num2 = b'класс'       # Не может записать в байтовый тип.
print(type(word_num2))
word_num3 = b'функция'
print(type(word_num3))
word_num4 = b'type'