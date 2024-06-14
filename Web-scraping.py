#!/usr/bin/env python
# coding: utf-8

# In[40]:


import pandas as pd
from bs4 import BeautifulSoup
import requests
import xlsxwriter


# In[12]:


HEADERS = ({'User-Agent':
           'add your own :)',
                           'Accept-Language': 'en-US, en;q=0.5'})
URL = 'http://www.imdb.com/chart/top'

data = requests.get(URL,headers=HEADERS)

if data.status_code != 200:
    print("Please check your url ")
else:
    soup = BeautifulSoup(data.content,'html.parser')
    print(soup)


# In[120]:


title = soup.find_all('h3', attrs={'class':'ipc-title__text'})
year = soup.find_all('span', attrs={'class':'sc-b189961a-8 kLaxqf cli-title-metadata-item'})
duration = soup.find_all('span', attrs={'class':'sc-b189961a-8 kLaxqf cli-title-metadata-item'})


# In[121]:


titles = []
years = []
durations = []
for t in title:
    titles.append(t.text)
    #years.append(y.text)
    #durations.append(d.text)

i = 0

for y in year:
   
    if(i%3 == 0):
        
        years.append(y.text)
    i += 1
i = 1

while(i < len(year)):
   
    durations.append(year[i].text)
    i += 3



# In[117]:


workbook = xlsxwriter.Workbook('movie3.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write(0, 0 ,'Movie name')
worksheet.write(0, 1 ,'Year')
worksheet.write(0, 2 ,'Duration')

row = 1
for i, j, k in zip(titles,years,durations):
    worksheet.write(row, 0 ,i)
    worksheet.write(row,  1 ,j)
    worksheet.write(row, 2 ,k)
    row += 1
workbook.close()




    


# In[119]:


data = pd.read_excel('movie3.xlsx') 
data


# In[ ]:




