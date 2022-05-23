# yandex.ru, youtube.com

import os
import platform
import subprocess
from chardet import detect

urls = ['ya.ru', 'vk.com']
code = '-n' if platform.system().lower() == 'windows' else '-c'


for item_url in urls:
    ur = ['ping',code, '4', item_url]
    ya_ping = subprocess.Popen(ur, stdout=subprocess.PIPE)
    for line in ya_ping.stdout:
        result = detect(line)
        print(result)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))



# response = os.popen(f'ping {ip_list}').read()
#
# # response = os.popen(f'ping ya.ru').read()
#
# print(response)
#
# result_encode = response.encode(encoding='cp1251')
# print(result_encode)
# result_decode = result_encode.decode(encoding='cp866')
#
#
# print(result_decode)