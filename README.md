# Exercício-C114-Eng.-de-Software

## Execução do Client-Servidor TCP 

1. Inicie o servidor executando o arquivo Servidor.py.

2. Em seguida, em um terminal separado, execute o arquivo main.py.

## Solução de Conflitos com a Porta (HOST)

Caso a porta especificada (ex.: 65432) já esteja em uso por outro processo, será necessário encerrá-lo manualmente para liberar o recurso. Siga os passos abaixo via terminal:

1. Identifique os processos utilizando a porta:

netstat -ano | findstr :65432

Isso exibirá o PID (Process ID) de qualquer processo ativo na porta 65432

2. Encerre o processo correspondente:

taskkill /PID <PID> /F

Substitua <PID> pelo número retornado no passo anterior.
