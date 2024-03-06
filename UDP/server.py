import socket
import random

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

def get_conversion_rate(currency):
    # Simulação de uma função que obtém a cotação atual da moeda
    # Aqui estamos apenas gerando um valor aleatório para fins de demonstração
    if currency == 'dolar':
        return random.uniform(4, 5)  # Simula cotação entre R$4 e R$5
    elif currency == 'euro':
        return random.uniform(5, 6)  # Simula cotação entre R$5 e R$6
    else:
        return None

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    message = data.decode()
    value, currency = message.split()
    conversion_rate = get_conversion_rate(currency)
    if conversion_rate is not None:
        converted_value = float(value) / conversion_rate
        response = f'O valor de R$ {value} em {currency} é aproximadamente {converted_value:.2f}'
        sock.sendto(response.encode(), addr)
    else:
        response = 'Moeda não suportada.'
        sock.sendto(response.encode(), addr)
