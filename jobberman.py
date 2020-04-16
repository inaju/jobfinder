from bs4 import BeautifulSoup
import requests

def jobs():
    url = 'https://www.jobberman.com/jobs/it-software?q=&industry[0]=technology'
    page=requests.get(url)
    soup=BeautifulSoup(page.content, 'html.parser')

    result = soup.find_all('article', class_='search-result')

    title_s=[]
    location_s=[]
    information_s=[]
    
    for jobs in result:
        title=jobs.find('h3').text.rstrip()
        location = jobs.find('div', class_='search-result__location').text.strip()
        information = jobs.find(
            'div', class_='search-result__content transform-y-center content-show--under-md').text.strip()
        
        title_s.append(title)
        location_s.append(location)
        information_s.append(information)
        
    zipped = list(zip(title_s, location_s, information_s))
        
    for i,j,k in zipped:
        print(i,j,k)
    
    return zipped
jobs()
