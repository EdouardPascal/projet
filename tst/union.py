#Fonction union
def union (a,b):
	i=0
	d=len(b)
	while i<d:
		a.append(b[i])	
		i+=1
	return a 
a=[1,2,3,4]
b=[2,4,5,6,7,8]
print(union(a,b))
	