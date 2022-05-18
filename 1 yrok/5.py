# yandex.ru, youtube.com
# 5
import os

ip_list = input("Введите IP адрес: ")

response = os.popen(f'ping {ip_list}').read()

# response = os.popen(f'ping ya.ru').read()

print(response)

result_encode = response.encode(encoding='cp1251')
print(result_encode)
result_decode = result_encode.decode(encoding='cp866')


print(result_decode)