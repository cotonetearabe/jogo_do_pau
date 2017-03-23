import random, time, os
from PIL import Image as img



def xoragora():
	r = random.randrange(1,20)
	for i in range(r):
		choice_of_pic = random.choice(["pics/Xoragora.jpg","pic/abs.jpg","pics/after_pau_dinner.jpg","pics/archer_pau.jpg","pics/beer_man.jpg","pics/cant_let_go.jpg","pics/cat_pau.jpg","pics/dark_pau.jpg","pics/db_pau.jpg","pics/pau_a_lot.jpg","pics/pau_pda.jpg","pics/pau_pda2.png","pics/pau_too_high.jpg","pics/soro_santo_grall.jpg","pics/third_pau.jpg","pics/toxic.jpg"])
		xoagora_img = img.open(choice_of_pic)
		xoagora_img.show()


xoragora()