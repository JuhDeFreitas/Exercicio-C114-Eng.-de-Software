from modulos.modulo_main import ModuloCliente

# Configurando a instancia para o moduloa main
cliente = ModuloCliente()

# Recebendo os dados de Horários do Servidor
horarios = cliente.fetch_horario()
print("Horários recebidos:", horarios)
