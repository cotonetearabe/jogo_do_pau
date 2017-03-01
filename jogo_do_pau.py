#!usr/bin/python3
'''
Em falta:
-Mais historia mais opçoes uma "teia" mais ligada e maior
-Um gui ou uma janela destacada para nao estar tao primitivo pelo menos (ver turtleworld) or tk
-Historia para preencher o jogo historias do pau são posivies

Ideias:
-Fazer qualquer coisa com as varias variaveis no final(estilo de consequencias por decisoes)
-Criar opcção de recomeçar o jogo se calhar dividir em mais funçoes para poder controlar jogo e mais tarde adicionar gui
-Criar um contador de jogo para ver quanto e que cada pessoa joga e parte para limpar

Bugs:
-bug no reconhecimento de str
'''
import math, random, os
from PIL import Image as img

def before():
	q = input('Queres voltar ao menu?(ç/n)')
	a = random.randrange(2,54)
	if q == 'ç' or q == 'Ç':
		print('\n\n\n\n\n\n\n\n\n' * a )
		start()
	elif q == 'n' or q == 'N':
		print('k...')
		before()
	else:
		print('idk')
		before()


def xoragora():
	xoagora_img = img.open("Xoragora.jpg")
	xoagora_img.show()

def start():
	x = input("Bem vindo ao jogo_do_pau.\n\nSe quiseres o start_the_game insere 0, the_game 1, tracadinho 2 um_vs_zero 3, quem_quer_ser_pau 4, xadrez 5: \n\n Bons Paus! cotonete.arabe\n\n")
	y = eval(x)
	if (y==0):
		start_the_game()
	elif (y==1):
		the_game()
	elif (y==2):
		tracadinho()
	elif (y==3):
		um_vs_zero()
	elif (y==4):
		quem_quer_ser_pau()
	elif (y==5):
		xadrez()
	else:
		start()


def start_the_game():
	y = input('Diz ai uma merda qualquer... : ')
	x = eval(y)
	if (type(x)==int):
		print('ok se quiseres ir por ai...')
		y = input("Queres continuar?(ç ou n)\n\n\n")
		if (y=='ç') or (y=='Ç'):
			print('Pega de mão direita, bebe, volta a encher e bebe outra vez\n\n')
			before()
		elif (y=='n') or (y=='N'):
			print('És um merdas bebe de mão direita, se te recusares, sai da mesa.\n\n')
		b = input('Bebeste?')
		if (b=='') or (b == 'Ç'):
			o = input('Queres jogar outra vez?')
			if (o=='ç') or (b=='Ç'):
				start_the_game()
			elif (o=='n') or (o=='N'):
				print('The Ban Hammer has spoken...')
				before()
			#Aqui podia-se por um if (bebeu) jogo continua ou não
			else:
				print('The Ban Hammer has spoken...')
				xoragora()
				start()
		else:
			print('Bem... ou és um atrasado de merda ou estas a espera do que?')
			xoragora()
			start()
	elif (type(x)==float):
		print('Ok peculiar...')
		rnd = random.randrange(0,99)
		print('Boas neste jogo caso queiras jogar poderas beber...')
		print('Só estou a avisar para depois não haver mariqueçes')
		quest = input('Queres jogar?(ç ou n)')
		if (quest=='ç') or (quest=='Ç'):
			n = float(input('Dá ai um n positivo menor que 100'))
			print('Ok vamos ver que numero escolheste em relação ao meu?')
			if (n==rnd) and (n<100):
				print('Vá foi igual, o teu numero, ', n, 'é igual a, ', rnd, '\nSe for igual bebes tu')
				before()
			elif (n>rnd) and (n<100):
				print('Foi maior, o teu numero, ', n, 'é maior que, ', rnd,'\nSe for maior e nao fores de EI, alguem do curso bebe... se fores de EI nem tens de ir buscar alguem como deve ser')
				before()
			elif (n<rnd) and (n<100):
				print('Foi menor, o teu numero, ', n, 'é menor que, ', rnd, '\nSe for menor e fores de EI não és obrigado a beber mas é encoranjado')
				before()
			else:
				print('Well... This is awkhard...')
				xoragora()
				before()
		elif (quest=='n') or (quest=='N'):
			print('Ok faggit...')
		else:
			xoragora()
			print('Bem... isto esta tudo bugado...')
	elif type(x) == str:
		print('Fds um gajo de humanidades...')
		#Por query de imagens a funcionar por enquanto nada
		before()
	else:
		print('Bem isto espumou-çe a 1ª...')
		xoragora()
		before()


def the_game():
	n = random.randrange(0,13)
	if n < 10:
		print("Oh! shit i lost the the game\n\n\nI should try again....")
		start()
	elif n > 10:
		print("Ok i got the game this time")
		o = input('Queres outra vez?')
		if (o=='ç') or (o=='Ç'):
			the_game()
		elif (o=='n') or (o=='N'):
			print('...')
			before()
		else:
			print('f..')
			xoragora()
			before()
	else:
		xoragora()
		before()

def tracadinho():
	pau = input("Pau? ç/n")
	if pau == 'ç' or pau == 'Ç':
		for i in range(10):
			print("Desta vez estou mesmo a rasca...\nVou me pirar de mansinho...\nNão volto aquela tasca, NÃO!...\nNão bebo mais traçadinho...")
			o = input('Queres outra vez?')
			if (o=='ç') or (o=='Ç'):
				tracadinho()
			elif (o=='n') or (o=='N'):
				print('...')
				start()
			else:
				xoragora()
				before()
	elif (pau=='n') or (pau=='N'):
		print("És uma desgraça para a UE...\n\n\n")
		before()
	else:
		xoragora()
		before()

def um_vs_zero():
	x = input('Quantos ciclos queres?: \n')
	y = eval(x)
	c_o = 0
	c_i = 0
	if (type(y)==int):
		for i in range(y):
			a = random.randrange(0,2)
			if a == 0:
				c_o += 1
			elif a == 1:
				c_i += 1
	if (c_o>c_i):
		print("\n\n\n0:", c_o, "1: ", c_i, "\nOs 0's ganharam...\nGanharam por", c_o - c_i, "\nDrink up!!!!")
	elif (c_o<c_i):
		print("\n\n\n\n0:", c_o, "1: ", c_i, "\nOs 1's ganharam...\nGanharam por",c_i - c_o,"\n\nDrink up!!!")
	before()

def quem_quer_ser_pau():
	x = (input('insere os nomes das as pessoas que estao ai e separa-as com virgulas(,) :').split(','))
	print(random.choice(x), '\n eu sei que estavam a espera que isto fosse tipo quem quer ser milionario\ncalma isto sou so eu a criar nao ha tempo para tudo se querem mais ajudem')
	before()

def xadrez():
	print("lel... bebe")
	k = input('Bebeste? (ç/n)')
	if (k=='ç') or (k=='Ç'):
		 print('Check')
		 xadrez()
	elif (k=='n') or (k=='N'):
		print('and next...')
		start()
	else:
		xoragora()
		print('Well ur retarded')
start()
