#!/usr/bin/env python
# coding: utf-8

# In[5]:


#1) Write a python program to display all the header tags from wikipedia.org and make data frame.
import pandas as pd
import requests
from bs4 import BeautifulSoup

url_link = 'https://en.wikipedia.org/wiki/Main_Page'
request = requests.get(url_link)
 
Soup = BeautifulSoup(request.text, 'lxml')
 
# creating a list of all common heading tags
heading_tags = ["h1", "h2", "h3"]
for tags in Soup.find_all(heading_tags):
    
    
    print(tags.name + ' -> ' + tags.text.strip())
    
    
    
    





    


# In[ ]:


#3) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame-
#a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.

#b) Top 10 ODI Batsmen along with the records of their team andrating.
#c) Top 10 ODI bowlers along with the records of their team andrating.

#4) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data frame-
#a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.

#b) Top 10 women’s ODI Batting players along with the records of their team and rating.
#c) Top 10 women’s ODI all-rounder along with the records of their team and rating.


import pandas as pd
from bs4 import BeautifulSoup
import requests



def Menu():
	print('\n1. Men \n2. Women\n')
	gen=Gender()
	print('\n1. Team Rankings \n2. Player Ranking\n')
	tp=TeamOrPlayer()
	
	mode=''
	val=''
	
	if gen=='mens':
		print('\n1. Test\n2. ODI\n3. T20\n')
		mode=Mode()

	if tp=='player-rankings':
		if mode=='':
			print('\n1. ODI\n2. T20\n')
			mode=Mode2()
		print('\n1. Batting\n2. Bowling\n3. All-Rounder\n')
		val=Value()
	
	return gen,tp,mode,val


def Gender():
	gender=input('Enter your choice:')
	code={'1':'mens','2':'womens'}

	if gender in code:
		return code[gender]
	
	else:
		print('\nInvalid Input\nTry Again\n')
		return Gender();


def TeamOrPlayer():
	choice=input('Enter your choice:')
	tp={'1':'team-rankings','2':'player-rankings'}
	
	if choice in tp:
		return tp[choice]
	
	else:
		print('\nInvalid Input\nTry Again\n')
		return TeamOrPlayer();

	
def Mode():
	choice=input('Enter your choice:')
	word={'1':'/test','2':'/odi','3':'/t20i'}
	
	if choice in word:
		return word[choice]
	
	else:
		print('\nInvalid Input\nTry Again\n')
		return Choice();


def Mode2():
	choice=input('Enter your choice:')
	word={'1':'/odi','2':'/t20i'}
	
	if choice in word:
		return word[choice]
	
	else:
		print('\nInvalid Input\nTry Again\n')
		return Choice();


def Value():
	choice=input('Enter your choice:')
	val={'1':'batting','2':'bowling','3':'all-rounder'}
	
	if choice in val:
		return val[choice]
	
	else:
		print('\nInvalid Input\nTry Again\n')
		return Value()


def URL():
	gen,tp,mode,val=Menu()
	url='https://www.icc-cricket.com/rankings/'+gen+'/'+tp+mode+'/'+val
	header=gen.upper() +' ' +mode[1:].upper() + ' ' + val.upper()
	print('\n{:<15}  {:<30}\n{:<15}  {:<30}'.format('',tp.upper(),'',header))
	return url,tp


def SOUP(url,tp):
	try:
		res=requests.get(url)
		soup=BeautifulSoup(res.text,'lxml')
		a= soup.find_all('tr',{'class':'table-body'})
		data={}
			
		for i in a :
			team=[]
			name=''
			rating=''

			try:
				rank=int(i.contents[1].text)
			except:
				pass
			
			try:	
				name=i.contents[3].text.replace('\n','')
				name=" ".join(name.split())
				if rank==1 and tp=='player-rankings':
					name=name[0:-3]
			except:
				pass

			try:
				rating=i.contents[9].text
			except:
				if rank==1 :
					rating=i.contents[5].text
				else:
					rating=i.contents[7].text
			
			team.extend([name,rating])
			data[rank]=team
		
		return data

	except:
		return SOUP(url,tp)


def Print(data):
	print('\nRANKING \t TEAM\t\t\t\tRATING')
	for i in sorted(data):
		print('{:<10}       '.format(i),end='')
		for j in range(len(data[i])):
			print('{:<26}'.format(data[i][j]),end='     ')
		print()


def main():
	
	url,tp=URL()
	data=SOUP(url,tp)
	Print(data)	


if __name__=='__main__':
	main()


# In[1]:


#5 Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world and make data frame-
#i) Headline
#ii) Time
#iii) News Link


import requests
from bs4 import BeautifulSoup
import pandas as pd
url='https://www.cnbc.com/world/?region=world'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
headlines = soup.find('body').find_all('h2')
for x in headlines:
print(x.text.strip())
Time = soup.find('body').find_all('time')
for x in Time:
    print(x.text.strip())
News_Link = soup.find('body').find_all('a')
for x in News_Link:
    print(x.text.strip())
    df = pd.DataFrame({'headlines':headlines,'Time':Time,'News_Link':News_Link}) 

    
    
    

    


# In[2]:


#6Write a python program to scrape the details of most downloaded articles from AI in last 90days.https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles
#Scrape below mentioned details and make data frame-
#i) Paper Title
#ii) Authors
#iii) Published Date
#iv) Paper URL



import requests
from bs4 import BeautifulSoup
import pandas as pd
url='https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
headlines = soup.find('body').find_all('h1')
for x in headlines:
print(x.text.strip())
Author = soup.find('body').find_all('span')
for x in Author:
    print(x.text.strip())
Published_date = soup.find('body').find_all('span')
for x in Published_date:
    print(x.text.strip())
Paper_URL = soup.find('body').find_all('a')
for x in Paper_URL:
    print(x.text.strip())
    df = pd.DataFrame({'headlines':headlines,'Author':Author,'Published_date':Published_date,'Paper_URL':Paper_URL}) 




# In[2]:


#7) Write a python program to scrape mentioned details from dineout.co.inand make data frame-
#i) Restaurant name
#ii) Cuisine
#iii) Location
#iv) Ratings
#v) Image URL

import requests
from bs4 import BeautifulSoup
import pandas as pd
url='https://www.dineout.co.in/delhi-restaurants/buffet-special'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
Restaurant_Name = soup.find('body').find_all('a')
for x in Restaurant_Name:
print(x.text.strip())
Cuisine = soup.find('body').find_all('span')
for x in Cuisine:
    print(x.text.strip())
location = soup.find('body').find_all('i')
for x in  location:
    print(x.text.strip())
Ratings = soup.find('body').find_all('div')
for x in  Ratings:
    print(x.text.strip())
Image_URL = soup.find('body').find_all('img')
for x in Image_URL:
    print(x.text.strip())

    df = pd.DataFrame({'Restaurant_Name':Restaurant_Name,'Cuisine':Cuisine,'location':location,'Ratings':Ratings,'Image_URL':Image_URL}) 



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




