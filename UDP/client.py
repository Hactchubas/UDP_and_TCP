import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

value = input("Digite o valor em reais $: ")
currency = input("Digite a moeda desejada (dolar ou euro): ")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(f"{value} {currency}".encode(), (UDP_IP, UDP_PORT))

data, addr = sock.recvfrom(1024)
print("Resposta do servidor:", data.decode())

sock.close()
