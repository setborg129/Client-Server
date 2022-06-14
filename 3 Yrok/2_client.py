from socket import socket, AF_INET, SOCK_STREAM


CLIENT_SOCK = socket(AF_INET, SOCK_STREAM)
CLIENT_SOCK.connect(('127.0.0.1', 8007))
MSG = 'Привет, сервер !'
CLIENT_SOCK.send(MSG.encode('utf-8'))
DATA = CLIENT_SOCK.recv(4096)
# print(f"Сообщение от сервера : {DATA.decode('utf-8')} длиной {len(DATA)} байт")
print(f"Сообщение от сервера : {DATA.decode('utf-8')}")
CLIENT_SOCK.close()