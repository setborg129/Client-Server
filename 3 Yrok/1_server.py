from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
import sys

SERV_IP = '127.0.0.1'
SERV_PORT = 8007
SERV_SOCK = socket(AF_INET, SOCK_STREAM)
SERV_SOCK.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
SERV_SOCK.bind((SERV_IP, SERV_PORT))
SERV_SOCK.listen(1)

try:
    while True:
        CLIENT_SOCK, ADDR = SERV_SOCK.accept()
        DATA = CLIENT_SOCK.recv(4096)
        print(f"Сообщение: {DATA.decode('utf-8')} было отправлено клиентом: {ADDR}")
        # MSG = 'Привет, клиент !'
        MSG = f"IP-адрес сервера - {SERV_IP} Порт: {SERV_PORT}"
        CLIENT_SOCK.send(MSG.encode('utf-8'))
        CLIENT_SOCK.close()
finally:
    SERV_SOCK.close()