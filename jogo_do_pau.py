'''
Bem vindo ao Jogo do Pau
Nem sempre tudo esta atualizado para jogar e necessario este script e a imagem Xoragora.jpg

Em falta:
-Implementar gif's no Xoragora()
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
import math, random, time
from PIL import Image as img


def before():
	q = input('Queres voltar ao menu?(ç/n)')
	a = random.randrange(2, 54)
	if q == 'ç' or q == 'Ç' or q == '':
		print('\n\n\n\n\n\n\n\n\n' * a)
		start()
	elif q == 'n' or q == 'N':
		print('k...')
		xoragora()
		before()
	else:
		print('idk')
		before()
		xoragora()


def xoragora():
	r = random.randrange(1, 15)
	for i in range(r):
		choice_of_error()
		choice_of_pic = random.choice(["pics/Xoragora.jpg", "pics/after_pau_dinner.jpg", "pics/archer_pau.jpg", "pics/beer_man.jpg", "pics/cant_let_go.jpg", "pics/cat_pau.jpg", "pics/dark_pau.jpg", "pics/db_pau.jpg", "pics/pau_a_lot.jpg", "pics/pau_pda.jpg", "pics/pau_pda2.png", "pics/pau_too_high.jpg", "pics/soro_santo_grall.jpg", "pics/third_pau.jpg", "pics/toxic.jpg"])
		xoagora_img = img.open(choice_of_pic)
		xoagora_img.show()
	start()


def choice_of_error():
		print("\n\n\n\n\n\n")
		print(random.choice(["\nf...\n", "Bem isto espumou-çe a 1ª...", "Bem... isto esta tudo bugado...", "Bem... ou és um atrasado de merda ou estas a espera do que?", "################\nThe Ban Hammer has spoken...\n################", "#####\nThis is an ERROR Message\n :) sorry\n#####", "\nERRRORRR BITCHES!!!\n", "\nThis is your fault PAY ME!\n", "\nGoogle cannot be reach at this moment...\n\nGET BACK IN YOUR CAGE PLEBIAN\n", "Hello i am jogo_do_pau\nI am a python game\nplz devolop me my dev sucks :(\n", "Nah dude, im way too drunk to play...\n", "##############\nWelcome to the matrix\nThey found you neo!\n##############\n\n\n ps: jk we're all in hell\n\n\n"]))
		print("\n\n")


def start():
	x = input("Bem vindo ao jogo_do_pau.\n\nSe quiseres o start_the_game insere 0, the_game 1, tracadinho 2 um_vs_zero 3, quem_quer_ser_pau 4, xadrez 5, quinta_feira 6, ate_ao_pau 7: \n\n Bons Paus! cotonete.arabe\n\n")
	y = eval(x)
	if (y == 0):
		start_the_game()
	elif (y == 1):
		the_game()
	elif (y == 2):
		tracadinho()
	elif (y == 3):
		um_vs_zero()
	elif (y == 4):
		quem_quer_ser_pau()
	elif (y == 5):
		xadrez()
	elif (y == 6):
		quinta_feira()
	elif (y == 7):
		ate_ao_pau()
	elif (y == 8):
		mane_mane()
	else:
		xoragora()
		start()


def start_the_game():
	y = input('Diz ai uma merda qualquer: ')
	x = eval(y)
	if (type(x) == int):
		print('ok se quiseres ir por ai...')
		y = input("Queres continuar?(ç ou n)\n\n\n")
		if (y == 'ç') or (y == 'Ç'):
			print('Pega de mão direita, bebe, volta a encher e bebe outra vez\n\n')
			before()
		elif (y == 'n') or (y == 'N'):
			print('És um merdas bebe de mão direita, se te recusares, sai da mesa.\n\n')
		b = input('Bebeste?')
		if (b == '') or (b == 'Ç'):
			o = input('Queres jogar outra vez?')
			if (o == 'ç') or (b == 'Ç'):
				start_the_game()
			elif (o == 'n') or (o == 'N'):
				print('The Ban Hammer has spoken...')
				before()
			else:
				print('The Ban Hammer has spoken...')
				xoragora()
				start()
		else:
			print('Bem... ou és um atrasado de merda ou estas a espera do que?')
			xoragora()
			start()
	elif (type(x) == float):
		print('Ok peculiar...')
		rnd = random.randrange(0, 99)
		print('Boas neste jogo caso queiras jogar poderas beber...')
		print('Só estou a avisar para depois não haver mariqueçes')
		quest = input('Queres jogar?(ç ou n)')
		if (quest == 'ç') or (quest == 'Ç'):
			n = float(input('Dá ai um n positivo menor que 100'))
			print('Ok vamos ver que numero escolheste em relação ao meu?')
			if (n == rnd) and (n < 100):
				print('Vá foi igual, o teu numero, ', n, 'é igual a, ', rnd, '\nSe for igual bebes tu')
				before()
			elif (n > rnd) and (n < 100):
				print('Foi maior, o teu numero, ', n, 'é maior que, ', rnd, '\nSe for maior e nao fores de EI, alguem do curso bebe... se fores de EI nem tens de ir buscar alguem como deve ser')
				before()
			elif (n < rnd) and (n < 100):
				print('Foi menor, o teu numero, ', n, 'é menor que, ', rnd, '\nSe for menor e fores de EI não és obrigado a beber mas é encoranjado')
				before()
			else:
				print('Well... This is awkhard...')
				xoragora()
				before()
		elif (quest == 'n') or (quest == 'N'):
			print('Ok faggit...')
		else:
			xoragora()
			print('Bem... isto esta tudo bugado...')
	elif type(x) == str:
		print('Fds um gajo de humanidades...')
		# Por query de imagens a funcionar por enquanto nada
		before()
	else:
		print('Bem isto espumou-çe a 1ª...')
		xoragora()
		before()


def the_game():
	n = random.randrange(0, 13)
	if n < 10:
		print("Oh! shit i lost the the game\n\n\nI should try again....")
		start()
	elif n > 10:
		print("Ok i got the game this time")
		o = input('Queres outra vez? ')
		if (o == 'ç') or (o == 'Ç'):
			the_game()
		elif (o == 'n') or (o == 'N'):
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
	pau = input("Pau?(ç/n): ")
	if pau == 'ç' or pau == 'Ç':
		for i in range(10):
			print("Desta vez estou mesmo a rasca...\nVou me pirar de mansinho...\nNão volto aquela tasca, NÃO!...\nNão bebo mais traçadinho..." + ("\n" * random.randrange(1, 15)))
			o = input('Queres outra vez? ')
			if (o == 'ç') or (o == 'Ç'):
				tracadinho()
			elif (o == 'n') or (o == 'N'):
				print('...')
				start()
			else:
				xoragora()
				before()
	elif (pau == 'n') or (pau == 'N'):
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
	if (type(y) == int):
		for i in range(y):
			a = random.randrange(0, 2)
			if a == 0:
				c_o += 1
			elif a == 1:
				c_i += 1
	else:
		xoragora()
	if (c_o > c_i):
		print("\n\n\n0:", c_o, "1: ", c_i, "\nOs 0's ganharam...\nGanharam por", c_o - c_i, "\nDrink up!!!!")
		before()
	elif (c_o < c_i):
		print("\n\n\n\n0:", c_o, "1: ", c_i, "\nOs 1's ganharam...\nGanharam por", c_i - c_o, "\n\nDrink up!!!")
		before()
	else:
		xoragora()


def quem_quer_ser_pau():
	x = (input('insere os nomes das as pessoas que estao ai e separa-as com virgulas(,) :').split(','))
	print(random.choice(x), '\n eu sei que estavam a espera que isto fosse tipo quem quer ser milionario\ncalma isto sou so eu a criar nao ha tempo para tudo se querem mais ajudem')
	before()


def xadrez():
	r_u = random.randrange(1, 100)
	r_g = random.randrange(1, 100)
	if (r_u < r_g):
		print("lel... bebe")
		k = input('Bebeste? (ç/n): ')
		if (k == 'ç') or (k == 'Ç'):
			print('Check')
			start()
		elif (k == 'n') or (k == 'N'):
			print('and next...')
			start()
		else:
			xoragora()
			print('Well ur retarded\n')
	elif (r_g < r_u):
		print("Parabéns! Podes mandar beber um admin/Paudre\n")
	else:
		xoragora()
	start()


def quinta_feira():
	r = random.randint(1, 9)
	for i in range(r):
		print("PAU! " * r)
		time.sleep(2)
	print("\n" * r)
	start()


def ate_ao_pau():
	print("BEBE ENQUANTO HÁ PAU!(3secs)\n\n")
	time.sleep(3)
	pau = random.randint(3, 15)
	for i in range(pau):
		print(pau * 'PAU! ')
		time.sleep(1)
	before()


def mane_mane():
	x = input("RUS?")
	if x == 'ç' or x == 'Ç':
		print("Goodbye my friend may the pau be with you")
	elif x == 'n' or x == 'N':
		print("I knew you could drink a little more!\nWelcome back!\n\n\n")
		start()
	else:
		print("Well fuck you then!!!")
		xoragora()
		start()


start()
