# test_modulo_servidor.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from unittest.mock import patch, MagicMock
from modulos.modulo_servidor import ModuloServidor
import socket


class TestModuloServidor(unittest.TestCase):

    def setUp(self):
        self.servidor = ModuloServidor()

    #CENARIOS DE SUCESSO
    # Testes para verificar a inicialização do socket
    @patch('socket.socket')
    def test_socket_init(self, mock_socket):
        mock_socket_instance = MagicMock()
        mock_socket.return_value = mock_socket_instance

        result = self.servidor.socket_init()

        mock_socket.assert_called_once_with(socket.AF_INET, socket.SOCK_STREAM)
        mock_socket_instance.bind.assert_called_once_with((self.servidor.host, self.servidor.port))
        mock_socket_instance.listen.assert_called_once()
        self.assertEqual(result, mock_socket_instance)

    # Verifica se a conexão foi estabelecida corretamente
    @patch('socket.socket')
    def test_aceitar_conexao_sucesso(self, mock_socket):
        mock_socket_instance = MagicMock()
        mock_conn = MagicMock()
        mock_addr = ('127.0.0.1', 12345)
        mock_socket_instance.accept.return_value = (mock_conn, mock_addr)

        self.servidor.server_socket = mock_socket_instance
        conn, addr = self.servidor.aceitar_conexao()

        self.assertEqual(conn, mock_conn)
        self.assertEqual(addr, mock_addr)

    #CENARIO DE FALHA
    # Verificando se a conexão foi aceita para um socket não configurado
    def test_aceitar_conexao_socket_nao_inicializado(self):
        with self.assertRaises(RuntimeError):
            self.servidor.aceitar_conexao()

if __name__ == '__main__':
    unittest.main()
