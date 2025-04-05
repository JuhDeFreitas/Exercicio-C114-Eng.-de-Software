import unittest
import json
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modulos.horario import Horario  # ajuste conforme o caminho real

class TestHorario(unittest.TestCase):

    def setUp(self):
        self.horario = Horario()


    def test_conteudo_dos_horarios(self):
        esperado = [
            {
                "nomeDoProfessor": "Prof. Christopher",
                "horarioDeAtendimento": "Seg 17:30 - 19:10",
                "periodo": "integral",
                "sala": "5",
                "predio": "1"
            },
            {
                "nomeDoProfessor": "Prof. Jonas",
                "horarioDeAtendimento": "Ter 19:30 - 21:10",
                "periodo": "noturno",
                "sala": "3",
                "predio": "14"
            }
        ]
        self.assertEqual(self.horario.horarios, esperado)

    # VErifica a conversão de unidades
    def test_to_json_string_retorna_string_valida(self):
        json_string = self.horario.to_json_string()
        self.assertIsInstance(json_string, str)

        # Testa se pode ser convertido de volta em lista com os mesmos dados
        dados = json.loads(json_string)
        self.assertEqual(dados, self.horario.horarios)

    # Verifica se todos os campos estão presentes no JSON
    def test_to_json_string_contem_campos_esperados(self):
        json_string = self.horario.to_json_string()
        self.assertIn("nomeDoProfessor", json_string)
        self.assertIn("horarioDeAtendimento", json_string)
        self.assertIn("periodo", json_string)
        self.assertIn("sala", json_string)
        self.assertIn("predio", json_string)

    def buscar_por_predio(self, predio):
      return [prof for prof in self.horarios if prof["predio"] == predio]


    #CENARIOS DE FALHA
    def test_to_json_string_falha_serializacao(self):
          class ObjetoNaoSerializavel:
              pass

          # Força a classe Horario a ter um dado inválido para json.dumps
          self.horario.horarios.append(ObjetoNaoSerializavel())

          with self.assertRaises(TypeError):
              self.horario.to_json_string()

    def test_sala_inexistente(self):
        # Simula uma sala inválida
        self.horario.horarios[0]["sala"] = "99"  # Supondo que sala 99 não exista

        salas_validas = [str(i) for i in range(1, 11)]  # Salas de "1" a "10"

        for item in self.horario.horarios:
            self.assertIn(
                item["sala"],
                salas_validas,
                msg=f"Sala inválida detectada: {item['sala']}"
            )  

    def test_professor_nao_existe(self):
      nomes = [prof["nomeDoProfessor"] for prof in self.horario.horarios]
      self.assertNotIn("Prof. Fantasma", nomes)   

    def test_predio_inexistente(self):
      predios = [prof["predio"] for prof in self.horario.horarios]
      self.assertNotIn("99", predios)  
  

if __name__ == '__main__':
    unittest.main()
