
import requests;
from Parser.Weather.Weather import api_token;
# one can obtain API_token on https://openweathermap.org/
url = "https://api.openweathermap.org/data/2.5/weather";

params = {
    "q":"Киев",
    "appid":api_token,
    "units":"metric"
}

headers = {

    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

session = requests.Session();

r = session.get(url, headers=headers,params=params);
src = r.json();


print(src['name']);



for i in src["weather"]:
    print ('Main weather params')
    print(i);


for i in range (1) :

    # keys = list(src['main'].keys());
    # values = list(src['main'].values());
    # print (values)
    # print (keys)

    pairs = list(src['main'].items());
    i+=1;
    print("Temp. С.,  Pressure Hpa,  Humidity %")
    print(pairs)

for i in range (1) :

    pairs = list(src['wind'].items());
    i+=1;
    print("Wind Speed,  Deg,  Gust")
    print(pairs)



#soxranim html v file с кодировкой ютф8

# with open("Weather.html","w", encoding="utf-8") as file:
#     src = file.write(src);
#     print(src)