import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005

value = input("Digite o valor em reais: ")
currency = input("Digite a moeda desejada (dolar ou euro): ")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT))
sock.sendall(f"{value} {currency}".encode())

data = sock.recv(1024)
print("Resposta do servidor:", data.decode())

sock.close()
