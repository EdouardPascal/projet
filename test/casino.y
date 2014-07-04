import os
from random import randrange
from math import ceil
argent_user= 1000
continuer=True
print "Vous commencer la partie avec"+argent_user
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
        if mise>argent:
            print "Vous n'avez pas asez d'argent"
        
    

                   
