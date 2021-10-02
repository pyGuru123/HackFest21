# States and capital

import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://www.mapsofindia.com/states/'
r = requests.get(url)


html = r.text
soup = BeautifulSoup(html,'html.parser')

table = soup.find('table',class_='tableizer-table')
trows = table.find_all('tr')
table_header = table.find('tr',class_='tableizer-firstrow')


headers = []
for i in table_header:
	headers.append(i.text)
headers = headers[:7]

states = []
capitals = []
area = []
population = []
language = []
lar_city = []
districts = []

trows.pop(0)
for i in trows:
	td = i.find_all('td')
	states.append(td[0].text.strip())
	capitals.append(td[1].text.strip())
	area.append(td[2].text.strip())
	population.append(td[3].text.strip())
	language.append(td[4].text.strip())
	lar_city.append(td[5].text.strip())
	districts.append(td[6].text.strip())

indices = [i for i in range(1,len(states)+1)]

all_lists = zip(states,capitals,area,population,language,lar_city,districts)
df = pd.DataFrame(list(all_lists),columns=headers,index=indices)
df.to_csv('states-capital.csv')
print(df)

# saving image
img_url = 'https://www.mapsofindia.com/maps/india/map-of-india-political.gif'
r = requests.get(img_url)
fname = img_url.split('/')[-1]
with open(fname,'wb') as f:
	f.write(r.content)
