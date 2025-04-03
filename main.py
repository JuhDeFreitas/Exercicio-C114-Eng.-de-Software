import socket
import json

HOST = '127.0.0.1'
PORT = 65432

def fetch_horario():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))  # Conecta ao servidor
        data = client_socket.recv(1024)  # Recebe a resposta

    json_data = data.decode()  # Decodifica a string JSON
    return json.loads(json_data)  # Converte para dicionário Python

# Testando a função

horarios = fetch_horario()
print("Horários recebidos:", horarios)
