import requests;
from bs4 import BeautifulSoup;
import json;
import lxml;

url = "https://ru.tap.az";
# headers = {
#     "Accept":"*/*",
#     "User-Agent":
#         "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
# }
# req = requests.get(url, headers=headers);
# src = req.text;

#soxranim html v file с кодировкой ютф8

# with open("tapaz.html","w", encoding="utf-8") as file:
#     src = file.write(src);


# теперь у нас готов файл для работы и мы закоментим код выше
# подготовим файл и скормим его нашему парсеру

with open("tapaz.html", encoding="utf-8") as file:
    src = file.read()
soup = BeautifulSoup(src, "lxml");
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
allCatDict[name] = fullLink;


with open ("allCatDict.json","w",encoding="utf-8") as file:
    json.dump(allCatDict, file, indent=4, ensure_ascii=False);
