import requests
from bs4 import BeautifulSoup
import pandas as pd


def extract(page, jobTitle, location):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
    url = f'https://www.indeed.co.in/jobs?q={jobTitle}&l={location}&start={page}&radius=100'
    print(url)
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


def transform(soup):
    divs = soup.find_all('div', class_='jobsearch-SerpJobCard')
    for item in divs:
        title = item.find('a').text.strip()
        company = item.find('span', class_='company').text.strip()
        rating = item.find_all('span', class_='ratingsDisplay')
        for i in rating:
            rating = i.find('span', class_='ratingsContent').text.strip()
        location = item.find('span', class_='location').text.strip()
        try:
            salary = item.find('span', class_='salaryText').text.strip()
        except:
            salary = ''
        summary = item.find('div', {'class': 'summary'}).text.strip().replace('\n', '')

        job = {title,
               company,
               salary,
               # 'summary': Job Description,
               rating,
               location
               }
        joblist.append(job)
    return


joblist = []

for i in range(0, 40, 10):
    print(f'Getting page, {i}')
    c = extract(i, 'data scientist', 'Ahmedabad')
    transform(c)

df = pd.DataFrame(joblist)
print(df.head())
df.to_csv('jobs.csv')
