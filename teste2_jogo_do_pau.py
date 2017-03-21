import itertools, random

def start_the_gamev2():
	deck = list(itertools.product(range(1,14),['Espadas','Copas','Ouros','Paus']))
	random.shuffle(deck)
	print(deck[0][0], "de", deck[0][1])
	n = 5
	while(n>3):
		for i in range(1):
			random.shuffle(deck)
			q = input("E achas que vai ser o que?(1 a 14)")
			print("Pois é:", str(deck[i][0]), "de", (deck[i][1]))
			if (i==q):
				print("Penalti! Parabéns!\n")
				n+=1
			elif (i<q):
				n -= 1
				print("A carta retirada")
			elif (i>q):
				n -= 1
				print("")
			else:
				#xoragora()
				pass


start_the_gamev2()
"""
		if (i==x):
			print("Penalti! Parabéns!\n")
			#fazer 
	contador = 0
		if (c==r):
			print('Penalti! Parabéns\nE volta a zero...')
			contador += 1
		elif (c<r):
			print('A carta é inferior a intrudozida, ', c, '\n Bebe: ', r-c)
		elif (c>r):
			print('A carta é superior a intrudozida, ', c, '\n Bebe: ', c-r)
		else:
			print("idk")
		c_u += r
		print(c_u)
		#funçao para ver quais cartas sairam e imprimir uma lista serve bem e rapido de fazer
		#print game board for (each) cycle
"""