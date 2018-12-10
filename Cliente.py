#######################################
#                                     #
#       JONI SCRIPTS APRESENTA        #
#                                     #
#######################################
#Cliente conexão simples chat com o servidor
#é isso
#Joni - 10/12/2018
import socket #biblioteca

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = '192.168.0.104'

porta = 777

cliente.connect((ip, porta))

try:
	while True:
		msg = raw_input() + '\n'
		cliente.send(msg)
		resposta = cliente.recv(2048)
		print (resposta) + '\n'
except Exception as erro:
	print ('Falha: ' + str(erro))
