import unittest
from unittest.mock import patch, MagicMock
from modulos.modulo_main import ModuloCliente
import json

# CENARIO DE SUCESSO
class TestModuloClienteSucesso(unittest.TestCase):

    @patch("socket.socket")
    def test_fetch_horario_recebe_lista(self, mock_socket_class):
        """
        Verifica se os dados recebidos são uma lista de dicionários.
        """
        mock_socket = MagicMock()
        mock_socket.recv.return_value = b'[{"nomeDoProfessor": "Prof. Chris", "sala": "2", "predio": "1"}]'
        mock_socket_class.return_value.__enter__.return_value = mock_socket

        cliente = ModuloCliente()
        result = cliente.fetch_horario()

        self.assertIsInstance(result, list)
        self.assertEqual(result[0]["nomeDoProfessor"], "Prof. Chris")

    @patch("socket.socket")
    def test_fetch_horario_sala_predio_correspondem(self, mock_socket_class):
        """
        Verifica se sala e prédio corretos são recebidos.
        """
        mock_socket = MagicMock()
        mock_socket.recv.return_value = b'[{"sala": "3", "predio": "1"}]'
        mock_socket_class.return_value.__enter__.return_value = mock_socket

        cliente = ModuloCliente()
        resultado = cliente.fetch_horario()
        self.assertEqual(resultado[0]["predio"], "1")

    @patch("socket.socket")
    def test_fetch_horario_com_campos_necessarios(self, mock_socket_class):
        """
        Verifica se todos os campos obrigatórios estão presentes.
        """
        mock_socket = MagicMock()
        mock_socket.recv.return_value = b'[{"nomeDoProfessor": "Prof. A", "horarioDeAtendimento": "Seg", "periodo": "integral", "sala": "1", "predio": "1"}]'
        mock_socket_class.return_value.__enter__.return_value = mock_socket

        cliente = ModuloCliente()
        data = cliente.fetch_horario()

        for campo in ["nomeDoProfessor", "horarioDeAtendimento", "periodo", "sala", "predio"]:
            self.assertIn(campo, data[0])

    @patch("socket.socket")
    def test_fetch_horario_varios_professores(self, mock_socket_class):
        """
        Verifica se múltiplos professores são recebidos corretamente.
        """
        mock_socket = MagicMock()
        mock_socket.recv.return_value = b'[{"nomeDoProfessor": "Prof. A", "sala": "2", "predio": "1"}, {"nomeDoProfessor": "Prof. B", "sala": "6", "predio": "2"}]'
        mock_socket_class.return_value.__enter__.return_value = mock_socket

        cliente = ModuloCliente()
        resultado = cliente.fetch_horario()

        self.assertEqual(len(resultado), 2)
        self.assertEqual(resultado[1]["predio"], "2")

    @patch("socket.socket")
    def test_fetch_horario_sucesso_json_valido(self, mock_socket_class):
        """
        Verifica se o JSON válido é processado corretamente.
        """
        mock_socket = MagicMock()
        mock_socket.recv.return_value = b'[{"nomeDoProfessor": "Prof. OK", "sala": "4", "predio": "1"}]'
        mock_socket_class.return_value.__enter__.return_value = mock_socket

        cliente = ModuloCliente()
        resultado = cliente.fetch_horario()
        self.assertEqual(resultado[0]["nomeDoProfessor"], "Prof. OK")

# CENARIO DE FALHA
class TestModuloClienteFalha(unittest.TestCase):

    @patch("socket.socket")
    def test_fetch_horario_conexao_recusada(self, mock_socket_class):
        """
        Simula erro de conexão recusada pelo servidor.
        """
        mock_socket = MagicMock()
        mock_socket.connect.side_effect = ConnectionRefusedError("Conexão recusada")
        mock_socket_class.return_value.__enter__.return_value = mock_socket

        cliente = ModuloCliente()
        with self.assertRaises(ConnectionRefusedError):
            cliente.fetch_horario()

    @patch("socket.socket")
    def test_fetch_horario_json_malformado(self, mock_socket_class):
        """
        Simula erro ao decodificar um JSON malformado.
        """
        mock_socket = MagicMock()
        mock_socket.recv.return_value = b'{"nomeDoProfessor": "Prof'  # JSON quebrado
        mock_socket_class.return_value.__enter__.return_value = mock_socket

        cliente = ModuloCliente()
        with self.assertRaises(json.JSONDecodeError):
            cliente.fetch_horario()

    @patch("socket.socket")
    def test_fetch_horario_lista_vazia(self, mock_socket_class):
        """
        Simula retorno de uma lista vazia.
        """
        mock_socket = MagicMock()
        mock_socket.recv.return_value = b'[]'
        mock_socket_class.return_value.__enter__.return_value = mock_socket

        cliente = ModuloCliente()
        resultado = cliente.fetch_horario()
        self.assertEqual(len(resultado), 0)

    @patch("socket.socket")
    def test_fetch_horario_predio_invalido(self, mock_socket_class):
        """
        Simula recebimento de um prédio fora do intervalo esperado.
        """
        mock_socket = MagicMock()
        mock_socket.recv.return_value = b'[{"sala": "2", "predio": "999"}]'
        mock_socket_class.return_value.__enter__.return_value = mock_socket

        cliente = ModuloCliente()
        resultado = cliente.fetch_horario()
        self.assertNotIn(resultado[0]["predio"], ["1", "2", "3", "4", "5", "6"])

    @patch("socket.socket")
    def test_fetch_horario_dado_nao_lista(self, mock_socket_class):
        """
        Simula retorno de um objeto JSON que não é uma lista.
        """
        mock_socket = MagicMock()
        mock_socket.recv.return_value = b'{"nomeDoProfessor": "Prof. A"}'  # JSON é um dicionário
        mock_socket_class.return_value.__enter__.return_value = mock_socket

        cliente = ModuloCliente()
        resultado = cliente.fetch_horario()
        self.assertNotIsInstance(resultado, list)

if __name__ == "__main__":
    unittest.main()
