import os

def minute(secondes):
	if secondes%60==0:
		minutes= secondes/60
		secondes=0
	else :
		minutes= secondes/60 
		secondes= secondes%60
	if minutes >60:
		if minutes%60==0:
			heures= minutes/60 
			minutes=0
		else :
			heures=minutes/60
			minutes= minutes%60
	else:
		pass
	if heures>24:
		if heures%24==0:
			jours=heures/24
			heures=0
		else:
			jours=heures/24
			heures= heures%24
	else: 
		pass
	return secondes, minutes,heures,jours


inputa= raw_input("Combien de secondes vous avez? \n")
secondes,minutes,heures,jours= minute(inputa)
print "Il est " +str(jours)+"jours et "+ str(heures)+" heures et "+ str(minutes)+ "minutes "+str(secondes)+" secondes"

