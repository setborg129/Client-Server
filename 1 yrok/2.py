# «class», «function», «method»
#2


# first_word = b'class'
# print(type(first_word))
# print(len(first_word))
#
# second_word = b'function'
# print(type(second_word))
# print(len(second_word))
#
# third_word = b'method'
# print(type(third_word))
# print(len(third_word))


A = 'class'
B = 'function'
C = 'method'
str_list = [A,B,C]

for item in str_list:
    el = eval(f'b"{item}"')
    el_tmp = (f"b'{item}'")
    print(el)
    print(el_tmp)
 # в данном примере я так и не понял зачем используется тут метод "eval", разницы я так и не увидел.

    # print('=' * 50)
    # print('type: ', type(el))
    # print(item)
    # print('in bytes:', len(el))


# Спасибо за пример. Теперь урок освоил.