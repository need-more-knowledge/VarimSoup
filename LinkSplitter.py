from urllib.parse import unquote

url = "https://zoon.ru/redirect/?to=https%3A%2F%2Fwww.credus.su%2F&hash=6b918003d1373975c576000c553fa6f5&from=57ce0b7040c0886b548b601f.b96b&ext_site=ext_site&backurl=https%3A%2F%2Fzoon.ru%2Fspb%2Fmedical%2Ftsifrovaya_stomatologiya_credus%2F";
url = unquote(url.split("?to=")[1].split("&")[0]);
print(url)