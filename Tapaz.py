import requests;
from bs4 import BeautifulSoup;
import json;
import lxml;

url = "https://ru.tap.az";
headers = {
    "Accept":"*/*",
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}
req = requests.get(url, headers=headers);
src = req.text;

#soxranim html v file с кодировкой ютф8

# with open("tapaz.html","w", encoding="utf-8") as file:
#     src = file.write(src);


# теперь у нас готов файл для работы и мы закоментим код выше
# подготовим файл и скормим его нашему парсеру

with open("tapaz.html", encoding="utf-8") as file:
    src = file.read()
soup = BeautifulSoup(src, "lxml");

# elec_href = url + soup.find("div",class_="header-categories-row").find("a").get("href");
# print(elec_href)
#
# cat_name = soup.find("div",class_="header-categories-row").find("a").find("span").text
# print(cat_name)
#
# electron_sub = soup.find("div",class_="header-subcategories-columns").find_all("a");
# print(electron_sub)

#ALL Electronica obyavi
All_href = soup.find(class_="header-subcategories-columns").find("a",class_ = "primary-subcategories-i").get("href");
print (url + All_href)
All_tr_name = soup.find("span",class_ = "primary-subcategories-i_name").text;
print(All_tr_name)
#
# #Sub cat names + links
# sub_cat_links = soup.find("div",class_="header-subcategories-columns")
# for i in sub_cat_links:
#     link = i.get("href");
#     name = i.find("span","primary-subcategories-i_name").text;
#     print(url + link)
#     print(name)