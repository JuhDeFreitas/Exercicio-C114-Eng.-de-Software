
from modulos.horario import Horario
from modulos.modulo_servidor import ModuloServidor
import json

def servidor():
    # Instanciando o gerador de dados
    dados_horario = Horario()
    json_response = dados_horario.to_json_string()    #JSON a ser enviado via servidor

    # Iniciando o servidor
    servidor = ModuloServidor(host='127.0.0.1', port=65432)
    servidor.socket_init()
    servidor.enviar_dado(json_response)

if __name__ == "__main__":
    servidor()
