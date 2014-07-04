import os
from random import randrange
from math import ceil
argent_user= 1000
continuer=True
print "Vous commencer la partie avec",argent_user
while continuer:
    nombre_mise=-1
    while nombre_mise<0 or nombre_mise>49:
        nombre_mise=input("Choisissez un nombre de 0 a 49")
        try:
            nombre_mise=int (nombre_mise)
        except ValueError:
            print "Vous n'avez pas saisi de nombre"
            nombre_mise=-1
            continue
        if nombre_mise<0:
            print "Ce nombre est negatif"
        if nombre_mise>49:
            print"Ce nombre est superieur a 49"
    mise=0
    while mise<=0 or mise>argent_user:
        mise=input ("Combien voulez vous misez?")
        try:
            mise=int(mise)
        except ValueError:
            print "Vous n'avez pas ecrit de nombre"
            continue
        if mise<=0:
            print"La mise ne vaut rien"
        if mise>argent_user:
            print "Vous n'avez pas asez d'argent"

    numero_gagnant= randrange(50)
    print "La roulette s'est arretee sur ...",numero_gagnant
    if numero_gagnant==nombre_mise:
        print "Vous avez gagne",mise*3,"$"
        argent_user+=mise*3
    elif numero_gagnant%2== nombre_mise%2:
        print "Vous avez gagne",ceil(mise*0.5)
        mise= ceil(mise *0.5 )
        argent_user+=mise
    else:
        print "Vous avez perdu"
        argent_user-=mise

    if argent_user<=0:
        print "Vous n'avez plus d'argent"
        continuer=False
  

os.system("pause")
    

                   
