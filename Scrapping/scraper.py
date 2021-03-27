#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup as soup

# In[100]:


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}

# In[101]:


html = requests.get(
    'https://www.glassdoor.co.in/Job/los-angeles-data-scientist-jobs-SRCH_IL.0,11_IC1146821_KE12,26.htm',
    headers=headers)
print(html.status_code)

# In[102]:


bsobj = soup(html.content, 'lxml')
# print(bsobj)


# In[ ]:


url_list = []
for i in range(1, 6):
    url = 'https://www.glassdoor.co.in/Job/los-angeles-data-scientist-jobs-SRCH_IL.0,11_IC1146821_KE12,26.htm?p=' + str(
        i)

# In[103]:


company_name = []
for company in bsobj.findAll('div', {'class': 'jobLink'}):
    company_name.append(company.a.text.strip())

print(company_name)

# In[104]:


job_title = []
for title in bsobj.findAll('div', {'class': 'jobContainer'}):
    job_title.append(title.findAll('a')[1].text.strip())

job_title

# In[105]:


location = []
for i in bsobj.findAll('div', {'class': 'jobInfoItem empLoc'}):
    location.append(i.span.text.strip())

location

# In[106]:


links = []
for i in bsobj.findAll('div', {'class': 'jobContainer'}):
    link = 'https://www.glassdoor.co.in' + i.a['href']
    links.append(link)

links

# In[107]:


description = []

for link in links:
    page = requests.get(link, headers=headers)
    bs = soup(page.content, 'lxml')
    for job in bs.findAll('div', {'id': 'JobDescriptionContainer'})[0]:
        description.append(job.text.strip())

# In[108]:


description

# In[ ]:




