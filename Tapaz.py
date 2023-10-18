import requests;
from bs4 import BeautifulSoup;
import json;
import lxml;

url = "https://ru.tap.az";

headers = {
    'authority': 'ru.tap.az',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
}
response = requests.get('https://ru.tap.az/', headers=headers)


src = response.text;

#soxranim html v file с кодировкой ютф8

with open("tapaz.html","w", encoding="utf-8") as file:
    src = file.write(src);


# теперь у нас готов файл для работы и мы закоментим код выше
# подготовим файл и скормим его нашему парсеру

with open("tapaz.html", encoding="utf-8") as file:
    src = file.read()
soup = BeautifulSoup(src, "lxml");
title = soup.title
print(title.string)
#
# #Electronics category name
# cat_name = soup.find("div",class_="header-categories-row").find("a").find("span").text
# print(cat_name)
#
# #Electronics href
# elec_href = url + soup.find("div",class_="header-categories-row").find("a").get("href");
# print(elec_href)
#
# # ALL Electronica obyavi
# All_href = soup.find(class_="header-subcategories-columns").find("a",class_ = "primary-subcategories-i").get("href");
# print (url + All_href)
# All_tr_name = soup.find("span",class_ = "primary-subcategories-i_name").text;
# print(All_tr_name)
#
# #Sub cat names + links
# sub_cat_links = soup.find("div",class_="header-subcategories-columns")
# for i in sub_cat_links:
#     link = i.get("href");
#     name = i.find("span","primary-subcategories-i_name").text;
#     print(url + link)
#     print(name)


# # #Transport category name
# transCatName = soup.find("a","header-category transport").find("span").text;
# print(transCatName);
#
# #Transport category URL
# transCatUrl = url + soup.find("a","header-category transport").get("href");
# print(transCatUrl)

# ALL Categories1

#створимо словник для запису даних
allCatDict ={};


allCatList1 = soup.find(class_="header-navigation").find(class_="l-center").find("div");
for i in allCatList1:
    link = i.get("href");
    if link:
        print(url + link);
    else:
        pass

    name = i.find("span").text;
    if name == "Детский мир":
        print(name);
        break;
    if name:
        print(name);

    try: fullLink = url + link;
    except: None


    #запишимо данні у словник
    allCatDict[name] = fullLink;

   # print(f"{name}:{link}"); - variant 3apisi printa c obyeden. 2-x peremennix





# ALL Categories2
allCatList2 = soup.find(class_="header-navigation").find(class_="l-center").find("div").find_next_sibling("div",class_="header-categories-row");

for i in allCatList2:
    link = i.get("href");
    if link:
        print(url + link);
    else:
        pass

    name = i.find("span").text;
    if name == "Магазины":
        print(name);
        break;
    if name == "Все объявления":
        pass;
    if name:
        print (name);

fullLink = url + link;

#ключем буде - НЕЙМ,  а значенням - ЛІНК
allCatDict[name] = fullLink;

#запишимо данні у словник із параметрами encoding="utf-8, indent=4, ensure_ascii=False
with open ("allCatDict.json","w",encoding="utf-8") as file:
    json.dump(allCatDict, file, indent=4, ensure_ascii=False);


# Pagination links


