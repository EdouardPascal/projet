import os
def afficher_decimale(nb):
	if type(nb) is not float:
		raise TypeError("Le parametre doit etre un flottant")
		nb=str(nb)
		partie_entiere, partie_decimale= nb.split(".")
		return ",".join([partie_entiere,partie_decimale[:3]])

lol= afficher_decimale(49.45899)
print lol
os.system("pause")