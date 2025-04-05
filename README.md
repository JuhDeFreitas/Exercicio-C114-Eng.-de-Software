# Exercício-C114-Eng.-de-Software

Caso a porta HOST esteja ocupada, feche todos os processos que estiverem rodando na porta via terminal de comando.
Para isso realize a seguinte processo 
Mostra todos os processos rodando na porta:
- netstat -ano | findstr : <PORTA>

Encerra um determinado processo:
- taskkill /PID <PID> /F

<PORTA> Número da porta utilizada (65432)
<PID> Número do processo a ser fechado