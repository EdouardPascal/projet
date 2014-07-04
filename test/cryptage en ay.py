import os 
pyg = 'ay'

original = raw_input('Entrez un mot :')

if len(original) > 0 and original.isalpha():
    print original
else:
    print 'vide'

mot=original.lower()
premiere= mot[0]

if premiere in "aeiou":
   nouveau_mot=mot+pyg
   
else:
    nouveau_mot=mot[1:]+premiere+pyg
    
print nouveau_mot
	
os.system("pause")