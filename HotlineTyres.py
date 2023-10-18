import requests;
from bs4 import BeautifulSoup;
import lxml;
import json;

url = "https://hotline.ua/ua/auto/avtoshiny-i-motoshiny/605868/";
# headers = {
#     "Accept":"*/*",
#     "User-Agent":
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
# }
# req = requests.get(url, headers=headers);
# src = req.text;
# #print(src);
#
# #soxranim html v file с кодировкой ютф8
# with open("Hotline_tyres205.html", "w", encoding="utf-8") as file:
#     file.write(src)

#теперь у нас готов файл для работы и мы закоментим код выше
#подготовим файл и скормим его нашему парсеру

with open("Hotline_tyres205.html", encoding="utf-8") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

all_205_55_R16_txt = soup.find_all(class_ = "list-item list-item--row")
href = soup.find(class_ = "list-item__info").find("a").get("href")



for i in all_205_55_R16_txt:
    all_products_dic = {};
    for item in all_205_55_R16_txt:
        item_text = item.text
        item_href = (item_text +" " + "https://hotline.ua" + href)
        print(item_href)

#sozdaem slovar gde klych - dannie tovata a znachenie -> ssylka
    all_products_dic[item_text] = item_href;

#сохраним нашу инфо в джейсон файл c такими параметрами

    with open("all_205_55_R16.json", "w",encoding="utf-8") as file:
        json.dump(all_products_dic, file, indent=4, ensure_ascii=False)

#   загрузим наш файл в переменную all_205_55_R16.json
with open("all_205_55_R16.json",encoding="utf-8") as file:
    all_205_55_R16 = json.load(file)
    print(all_205_55_R16)

for category_name in all_205_55_R16:
    rep = [",", " ", "/n"," ' "," - "]
    for item in rep:
        if item in category_name:
            category_name = category_name.replace(item, " ")
            print(category_name)