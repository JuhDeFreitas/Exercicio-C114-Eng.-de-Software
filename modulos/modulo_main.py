import socket
import json

class ModuloCliente:
    def __init__(self, host='127.0.0.1', port=65432):
        self.host = host
        self.port = port

    def fetch_horario(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((self.host, self.port))
            data = client_socket.recv(1024)

        json_data = data.decode()
        return json.loads(json_data)
