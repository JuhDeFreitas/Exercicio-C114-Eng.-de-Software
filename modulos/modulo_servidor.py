# modulo_servidor.py
import socket

class ModuloServidor:
    def __init__(self, host='127.0.0.1', port=65432):
        self.host = host
        self.port = port
        self.server_socket = None

    def socket_init(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print(f"Servidor rodando em {self.host}:{self.port}...")
        return self.server_socket

    def aceitar_conexao(self):
        if not self.server_socket:
            raise RuntimeError("Socket não inicializado. Chame socket_init() antes.")
        conn, addr = self.server_socket.accept()
        print(f"Conexão recebida de {addr}")
        return conn, addr

    def enviar_dado(self, dado_em_string):
        while True:
            try:
                conn, addr = self.aceitar_conexao()
                print(f"Enviando dados para {addr}...")
                conn.sendall(dado_em_string.encode())
                print("Dados enviados com sucesso.")
                conn.close()
            except KeyboardInterrupt:
                print("\nServidor encerrado manualmente.")
                break
