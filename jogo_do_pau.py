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
from commonFunctions import errors, choice_of_error


def printPoints():
	pass
	# Print points per player


def main():
	pass
	print("Bem vindo ao jogo_do_pau!\nEsta versao e um jogo baseado em turnos")
	global players
	players = []
	qplayers = input('Insere os nomes dos jogadores separados por virgulas:').split(',')
	for p in qplayers:
		players = [p, 0]


if __name__ == '__main__':
	main()
