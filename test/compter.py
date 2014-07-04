import os

def count_string(mot):
	longueur=0
	mot = mot.split(" ")
	print mot
	for i in  mot:
		longueur = longueur + len(i)
	return longueur
print (count_string('Michael le grand'))

os.system('pause')