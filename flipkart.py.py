from requests import session
from bs4 import BeautifulSoup as BS
import pandas
s = session()
import requests

cookies = {
    'T': 'TI171075284605200173042070709474908058888440629489383666367085658902',
    'rt': 'null',
    'K-ACTION': 'null',
    '_pxvid': '22adfe0a-e507-11ee-b5b4-131c756a831e',
    'ud': '4.SLO_rUfvG4BQFKWBXSOFcJYMQfl6pc6q3KaArgK8a7glUkDyuurvT7VhWf2AztqrOJ23PkOlWhZm2gYnCgjH6OLeyZy_D8JQjJ2Fb2FtsBmrOkf0kC3zmfOEbsimfGY0BWLyc6pgqPHYfPcHGJauxw',
    'at': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjFkOTYzYzUwLTM0YjctNDA1OC1iMTNmLWY2NDhiODFjYTBkYSJ9.eyJleHAiOjE3MTYxODU3OTAsImlhdCI6MTcxNDQ1Nzc5MCwiaXNzIjoia2V2bGFyIiwianRpIjoiNTQ3YjkxMzUtMjlhOS00ODQ1LTgwNGQtZDk3MDE1ODk2ODI1IiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNzEwNzUyODQ2MDUyMDAxNzMwNDIwNzA3MDk0NzQ5MDgwNTg4ODg0NDA2Mjk0ODkzODM2NjYzNjcwODU2NTg5MDIiLCJrZXZJZCI6IlZJQzQwMTBCNTJBNEM3NEVFQkI1QjA5NDhENjcwNjkwMzUiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJDSCIsIm0iOnRydWUsImdlbiI6NH0.8LZXlNDGDUltyMjfExAnj8_n6-_WjJeMXAKoKJAArsc',
    'dpr': '1.7999999523162842',
    'vh': '799',
    'vw': '1371',
    'vd': 'VIC4010B52A4C74EEBB5B0948D67069035-1710752932989-58.1715266084.1715266084.156407696',
    'AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg': '1',
    'Network-Type': '4g',
    'AMCV_17EB401053DAF4840A490D4C%40AdobeOrg': '-227196251%7CMCIDTS%7C19853%7CMCMID%7C63046155935258145312986722536886938293%7CMCAID%7CNONE%7CMCAAMLH-1715405907%7C12%7CMCAAMB-1715870886%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCOPTOUT-1715273286s%7CNONE',
    'qH': '314cb5ed00b2e4a5',
    'pxcts': '2690e4c5-0e13-11ef-b1f7-2871b587c80f',
    'S': 'd1t10ViI/Pz89Yy4/EBw/Aj8/PwgtHx/4tnJ0rmad1sAxUvrwRSHsAUo79eVIkHGX9a3gVxgcd3sXYkKiwnzsS7Ns7A==',
    '_px3': '193f947e7b9295dee61bcb37038a9906043939c86010fcf764c733016fa56612:fQlPtsxMAPX+IZVbJGBLKrsVmbvL1bTwlOWgHaYYpJxeqItIXTkIVkIv2g34pX7pXEGcTpKBt6JGGFwI85Pd4Q==:1000:vUJgRV/b2Povbr4FuIAG0rH4CyvNSDQvGxEgF6k9nAQ4owjpssciCZOewtl+8h6sUGQ/zFv3KwRmWew8TlTXXGOlcnIrnpCtpFDGHA1ZOoreJpuxROcMmWUQuAqZAbsC+AuXv+Q6mZp4+RQvo0Srni5ndh5mwEyrCJeLHeIQq1qFWDdqKuSQbrPAnoUPjcvSi5MZ+Y7rhaAH5kq+smRC3+6xr23i/s9E9KAgJrjizDw=',
    'SN': 'VIC4010B52A4C74EEBB5B0948D67069035.TOK45A9EA6989F6498CB5AB1B2C59C25673.1715266093.LO',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'T=TI171075284605200173042070709474908058888440629489383666367085658902; rt=null; K-ACTION=null; _pxvid=22adfe0a-e507-11ee-b5b4-131c756a831e; ud=4.SLO_rUfvG4BQFKWBXSOFcJYMQfl6pc6q3KaArgK8a7glUkDyuurvT7VhWf2AztqrOJ23PkOlWhZm2gYnCgjH6OLeyZy_D8JQjJ2Fb2FtsBmrOkf0kC3zmfOEbsimfGY0BWLyc6pgqPHYfPcHGJauxw; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjFkOTYzYzUwLTM0YjctNDA1OC1iMTNmLWY2NDhiODFjYTBkYSJ9.eyJleHAiOjE3MTYxODU3OTAsImlhdCI6MTcxNDQ1Nzc5MCwiaXNzIjoia2V2bGFyIiwianRpIjoiNTQ3YjkxMzUtMjlhOS00ODQ1LTgwNGQtZDk3MDE1ODk2ODI1IiwidHlwZSI6IkFUIiwiZElkIjoiVEkxNzEwNzUyODQ2MDUyMDAxNzMwNDIwNzA3MDk0NzQ5MDgwNTg4ODg0NDA2Mjk0ODkzODM2NjYzNjcwODU2NTg5MDIiLCJrZXZJZCI6IlZJQzQwMTBCNTJBNEM3NEVFQkI1QjA5NDhENjcwNjkwMzUiLCJ0SWQiOiJtYXBpIiwidnMiOiJMTyIsInoiOiJDSCIsIm0iOnRydWUsImdlbiI6NH0.8LZXlNDGDUltyMjfExAnj8_n6-_WjJeMXAKoKJAArsc; dpr=1.7999999523162842; vh=799; vw=1371; vd=VIC4010B52A4C74EEBB5B0948D67069035-1710752932989-58.1715266084.1715266084.156407696; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; Network-Type=4g; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19853%7CMCMID%7C63046155935258145312986722536886938293%7CMCAID%7CNONE%7CMCAAMLH-1715405907%7C12%7CMCAAMB-1715870886%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCOPTOUT-1715273286s%7CNONE; qH=314cb5ed00b2e4a5; pxcts=2690e4c5-0e13-11ef-b1f7-2871b587c80f; S=d1t10ViI/Pz89Yy4/EBw/Aj8/PwgtHx/4tnJ0rmad1sAxUvrwRSHsAUo79eVIkHGX9a3gVxgcd3sXYkKiwnzsS7Ns7A==; _px3=193f947e7b9295dee61bcb37038a9906043939c86010fcf764c733016fa56612:fQlPtsxMAPX+IZVbJGBLKrsVmbvL1bTwlOWgHaYYpJxeqItIXTkIVkIv2g34pX7pXEGcTpKBt6JGGFwI85Pd4Q==:1000:vUJgRV/b2Povbr4FuIAG0rH4CyvNSDQvGxEgF6k9nAQ4owjpssciCZOewtl+8h6sUGQ/zFv3KwRmWew8TlTXXGOlcnIrnpCtpFDGHA1ZOoreJpuxROcMmWUQuAqZAbsC+AuXv+Q6mZp4+RQvo0Srni5ndh5mwEyrCJeLHeIQq1qFWDdqKuSQbrPAnoUPjcvSi5MZ+Y7rhaAH5kq+smRC3+6xr23i/s9E9KAgJrjizDw=; SN=VIC4010B52A4C74EEBB5B0948D67069035.TOK45A9EA6989F6498CB5AB1B2C59C25673.1715266093.LO',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-full-version': '"124.0.6367.119"',
    'sec-ch-ua-full-version-list': '"Chromium";v="124.0.6367.119", "Google Chrome";v="124.0.6367.119", "Not-A.Brand";v="99.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"macOS"',
    'sec-ch-ua-platform-version': '"14.3.1"',
}

params = {
    'q': 'iphone 13 ',
    'otracker': 'search',
    'otracker1': 'search',
    'marketplace': 'FLIPKART',
    'as-show': 'on',
    'as': 'off',
    'as-pos': '1',
    'as-type': 'HISTORY',
    'as-backfill': 'on',
}

response = requests.get('https://www.flipkart.com/search', params=params, cookies=cookies, headers=headers)
s.headers.update(headers)

def list_page():
    soup = BS (response.text,"html.parser")
    for i in soup.find_all("a","CGtC98"):
        links = "https://www.flipkart.com"+i.get("href")
        # print(links)
        detail_page(links)
    # next_page = soup.find("nav", "WSL9JP")
    # if next_page:
    #     next_page = [page.get("href") for page in next_page.find_all("a") if "next" in page.text.strip().lower()]
    #     if next_page:
    #        next_url = "https://www.flipkart.com" + next_page[0]
    #     list_page(next_url)
        #    print(next_url)

def detail_page(flipkart_data):
    list_all = [ ]
    list_1 = [ ]
    list_2 = [ ]
    r = s.get(flipkart_data)
    # print(r.url)
    soup = BS (r.text,"html.parser")
    try:
       name = soup.find("span","VU-ZEz").text
    except:
       name = None  
    try:   
      price = soup.find("div","Nx9bqj CxhGGd").text  
    except:
        price = None
    try:      
        rating = soup.find("div","XQDdHH").text
    except:
        rating = None
    try:      
        description = soup.find("div","yN+eNk w9jEaj").text
    except:
        description = None   
    try:   
        for i in soup.find("table","_0ZhAN9").find_all("tr"):       
            if len(i.find_all("td"))==2:
              key = i.find_all("td")[0]
              value = i.find_all("td")[1]
              table = ("{} : {}".format(key.text.strip(),value.text.strip())) 
              list_1.append(table)
    except:
        table = None
              
    item = dict()
    item ["title"] = name
    item ["rate"] = price
    item ["review"] = rating
    item ["pro_details"] = description
    item ["table"] = list_1
    list_all.append(item)
    print(list_all)       

list_page()        