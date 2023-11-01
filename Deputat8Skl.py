import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By



import requests

# headers = {
#     'Accept': 'text/css,*/*;q=0.1',
#     'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
#     'Cache-Control': 'no-cache',
#     'Connection': 'keep-alive',
#     'Pragma': 'no-cache',
#     'Referer': 'https://w1.c1.rada.gov.ua/',
#     'Sec-Fetch-Dest': 'style',
#     'Sec-Fetch-Mode': 'no-cors',
#     'Sec-Fetch-Site': 'same-site',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
#     'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
# }
#
# response = requests.get('https://w1.c1.rada.gov.ua/pls/site2/p_deputat_list?skl=9', headers=headers)
# src = response.text
# print(src)


baseUrl = "https://w1.c1.rada.gov.ua/pls/site2/p_deputat_list"
# def get_source_html(baseUrl):
#
#
#
#     try:
#         driver = webdriver.Chrome()
#         time.sleep(2)
#         driver.get(baseUrl)
#         driver.maximize_window()
#         time.sleep(6)
#         dept8 = driver.find_element(By.XPATH,"//a[@id='btnAllMPS']");
#         dept8.click();
#
#
#
#         time.sleep(6)
#         with open("Source-depu8.html", "w",encoding = 'UTF8') as file:
#                          file.write(driver.page_source)
#
#     except Exception as _ex:
#         print(_ex )
#     finally:
#         driver.close()
#         driver.quit()

# Збираємо всі посилання на профайли і зберігаємо в текстовик
file_path = 'Source-depu8.html'

def get_depu_urls(file_path):
    with open(file_path, encoding ='UTF-8') as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    dep_links = soup.find("ul",class_="search-filter-results search-filter-results-thumbnails").find_all("li")
    dep_urls = []
    for li in dep_links:
     urls = li.find("p",class_="title").find("a").get("href")
     dep_urls.append(urls)


    with open("UrlDepList.txt", "w",encoding = "UTF-8") as file:
        for url in dep_urls:
            file.write(f"{url}\n")




get_depu_urls(file_path)

