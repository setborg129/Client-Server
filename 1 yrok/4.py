# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard»
# из строкового представления в байтовое и выполнить обратное преобразование
# (используя методы encode и decode).
#4

first_word = 'разработка'
second_word = 'администрирование'
third_word = 'protocol'
four_word = 'standard'

def bytes_encode(str_bytes):
    return str_bytes.encode()

def bytes_decode(str_bytes):
    return str_bytes.decode()

#########################################
encode_byte = bytes_encode(first_word)
print(encode_byte)
decode_byte = bytes_decode(encode_byte)
print(f'{decode_byte}\n')
########################################

encode_byte = bytes_encode(second_word)
print(encode_byte)
decode_byte = bytes_decode(encode_byte)
print(f'{decode_byte}\n')

encode_byte = bytes_encode(third_word)
print(encode_byte)
decode_byte = bytes_decode(encode_byte)
print(f'{decode_byte}\n')

encode_byte = bytes_encode(four_word)
print(encode_byte)
decode_byte = bytes_decode(encode_byte)
print(f'{decode_byte}\n')