import socket
import json

# Definição do host e porta
HOST = '127.0.0.1'
PORT = 65432

horarios = {
    "nomeDoProfessor": "Prof. Christopher",
    "horarioDeAtendimento": "Seg 17:30 - 19:10",
    "periodo": "integral",
    "sala": "5",
    "predio": "1"
},{
    "nomeDoProfessor": "Prof. Jonas",
    "horarioDeAtendimento": "Ter 19:30 - 21:10",
    "periodo": "noturno",
    "sala": "3",
    "predio": "14"
}

# JSON que será enviado como resposta
json_response = json.dumps(horarios)

# Criando o socket do servidor (IPv4, TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Servidor rodando em {HOST} : {PORT}...")

while True:
    conn, addr = server_socket.accept()  # Aguarda conexão de um cliente
    print(f"Conexão recebida de {addr}")

    conn.sendall(json_response.encode())  # Envia o JSON como string
    print("JSON enviado!")

    conn.close()  # Fecha a conexão
