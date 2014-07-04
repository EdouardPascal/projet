import os

def product_list (liste):
	i=0
	s=1
	while i<len(liste) - 1:
		s=s*liste[i]
		i+=1
	return s
	
liste-[2,3,4]
print(product_list(liste))

os.system("pause")
