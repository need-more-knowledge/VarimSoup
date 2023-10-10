import requests
from bs4 import BeautifulSoup as bs

headers = {'accept':'*/*',
           'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
base_url ='https://hh.ru/vacancies/qa_engineer'
def hh_parse(base_url, headers):
    session = requests.Session();
    request = session.get(base_url, headers=headers);
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        divs = soup.find_all('div', attrs={'data-qa':'vacancy-serp__vacancy vacancy-serp__vacancy_standard_plus'})
        for div in divs:
            title = div.find('a', attrs ={'data-qa':'serp-item__title'}).text
            company = div.find('a',attrs = {'data-qa':'vacancy-serp__vacancy-employer'}).text
            href = div.find('a', attrs ={'data-qa':'serp-item__title'})['href']
            print (title)
            print(company)
            print (href)
            print ('/////////////////////////////////////////////////')
    else:
        print('ERROR')

hh_parse(base_url, headers)