#""" Code pour afficher 
#les liens d'une page"""
import os

def get_next_target(page): #fonction pour afficher les liens d'une page
	d_link = page.find('href=')
	m_link=page.find('"',d_link) 
	f_link=page.find('"', m_link+1)
	url=page[m_link+1:f_link]
	return url, f_link
	

def save_all_links(page): #fonction pour afficher les liens d'une page
	link=[]
	while True:
		url,end_pos = get_next_target(page)

		if url:  
			if 'http' in url:
				link.append(url) 
				page = page[end_pos:]
			else:
				page = page[end_pos:]
		else  :
			return link 

page = open('home.htm','r') 
a = page.read()

site=save_all_links(a)
liens=open("liens.txt",'w')
for i in site:
 liens.write(i + '\n')
liens.close()
recherche=raw_input("Que recherchez-vous?\n")

def search(site,recherche):
	fois=[]
	for result in site:
		if  recherche in result:
			fois.append(1)
			print result+ '\n'
		else:
			pass
	if fois =="":
		print ("ce lien n'existe pas")
	else:
		pass
			
search (site,recherche)
os.system('Pause')
