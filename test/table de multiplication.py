# -*-coding:Latin-1 -*
def table(nb):
    """Fonction affichant la table de multiplication par nb de 1 * nb jusqu'à max * nb"""
    i = 0
    while i < 10:
        print i + 1, "*", nb, "=", (i + 1) * nb
        i += 1
nombre= input("entrez le nombre\n")
table(nombre)
