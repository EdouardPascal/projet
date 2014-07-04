import os

informations= open("informations.txt",'w')
nom= raw_input("Quel est votre nom \n")
prenom= raw_input("Quel est votre prenom\n")
classe=raw_input("Quel est votre classe\n")
stockage=nom+" \n"+prenom+" \n"+classe
informations.write(stockage)
informations.close()
os.system("pause")
