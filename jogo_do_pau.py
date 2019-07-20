'''
Bem vindo ao Jogo do Pau
Nem sempre tudo esta atualizado para jogar e necessario este script e a imagem Xoragora.jpg

Em falta:
-Mais historias mais opçoes uma "teia" mais ligada e maior

Ideias:
-Fazer qualquer coisa com as varias variaveis no final(estilo de consequencias por decisoes)
-Criar opcção de recomeçar o jogo se calhar dividir em mais funçoes para poder controlar jogo e mais tarde adicionar gui
-Criar um contador de jogo para ver quanto e que cada pessoa joga e parte para limpar

como lidar com a questao de varios jogadores nas funçoes normais
'''
# math
# from commonFunctions import errors, choice_of_error
from commonFunctions import *


def printPoints():
	pass
	# Print points per player


def main():
	print("Bem vindo ao jogo_do_pau!\nEsta versao e um jogo baseado em turnos")
	global players
	players = []
	qplayers = input('Insere os nomes dos jogadores separados por virgulas:').split(',')
	for p in qplayers:
		# players += [p.strip(' '), 0]
		players.append([p, 0])
	print(players)
	while 1:
		for i, p in enumerate(players):
			print(f"Agora a jogar: {p} com {players[i][1]} pontos")
			q = input("O jogador pode passar este turno em troca de ir a casa de banho escrevendo: pass")
			if q == 'pass' or q == 'pass'.capitalize():
				print("Ok nenhum ponto adicionado")
			else:
				start()
				players[i][1] += 100

	"""
	"""


if __name__ == '__main__':
	main()
