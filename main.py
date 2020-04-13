import requests
from bs4 import BeautifulSoup
#this part gets the Html from the site
url = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=nigeria'
page=requests.get(url)

#beautiful soup allow me to search through the html content
soup = BeautifulSoup(page.content, 'html.parser')
#here i found the Div called ResultContainer, thats where i all the job listings are
results = soup.find(id='ResultsContainer')

jobs_elem=results.find_all('section',  class_='card-content')
    
#this function scrapes a website and returns a set of job listings in lists
def job_listings():
    title_list = []
    company_list=[]
    
    #it loops over jobs_elem and looks for the title, location and company's attached to the job
    for jobs in jobs_elem:
        title = jobs.find('h2', class_='title')
        company = jobs.find('div', class_='company')
        location = jobs.find('div', class_='location')

        #I noticed that sometimes it brought none, so i decided to allow it to continue
        if None in (title, company, location):
            continue

        #every iteration is added to the list
        title_list.append(title.text)
        company_list.append(company.text)

        # \n and \r are removed(stripped)
    job_listings.title_list_stripped = []
    job_listings.company_list_stripped = []
    
    for i in title_list:
        job_listings.title_list_stripped.append(i.rstrip())
        
    for i in company_list:
        job_listings.company_list_stripped.append(i.strip())
    

def main():
    
    list_to_dict={
        'title': '',
        'company': '',
    }
    
    job_listings()
    company = job_listings.company_list_stripped
    title = job_listings.title_list_stripped
    
    
main()
        
