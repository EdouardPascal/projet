import os

def plus_grand(liste):
	nb=0
	for el in liste:
		if el > nb:
			nb=el
		else:
			pass
	return nb
	
liste=[2,9,20,10]
print (plus_grand(liste))

os.system("pause")
	