import os
mauvais=[" ","!","_"]
def separation(liste):
	a=[]
	
	for z in liste:
		if z in  liste.split("!"+ "!"+"_") :
			pass
		else:
			a.append(z)
	return a
print separation ("Je suis_le ! plus, beau!")

os.system('pause')
