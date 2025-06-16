from requests import session
from bs4 import BeautifulSoup as BS
import pandas as pd
s = session()

import requests

cookies = {
    '_gcl_au': '1.1.567078259.1718106242',
    '_fbp': 'fb.1.1718106243533.999826387763443263',
    '__rtbh.lid': '%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22Dcs2L15Hm5653wbhLp9U%22%7D',
    'cdp-fngId': 'd68513ca939bc5ef0617e7ed6a77feb7',
    'cdp-Device-Id': 'e90d6ca6-27e7-11ef-9e64-f2bcb77acdd0',
    'cdp-mapperId': '1',
    '_hjSessionUser_451981': 'eyJpZCI6ImU0NGYyNTY0LWM1ZjYtNTNjOC1iZTI5LTYzM2JjNmM2YTg2NSIsImNyZWF0ZWQiOjE3MTgxMDYyNDcwMzMsImV4aXN0aW5nIjp0cnVlfQ==',
    'impressionDelayTime': '1000',
    'fnp_aton': 'N',
    'AMCVS_43C357DF589484E40A495D80%40AdobeOrg': '1',
    'AMCV_43C357DF589484E40A495D80%40AdobeOrg': '179643557%7CMCIDTS%7C19889%7CMCMID%7C52668679803917176142847477469811606077%7CMCAAMLH-1718950972%7C12%7CMCAAMB-1718950972%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1718353372s%7CNONE%7CvVersion%7C5.5.0',
    'localCurrency': 'INR',
    '_gid': 'GA1.2.558609106.1718346174',
    'uscnlg': 'true',
    's_cc': 'true',
    'AMO-tid': '317833169',
    'usid': '1247768968',
    '_hjSession_451981': 'eyJpZCI6IjFkNmVhZjA2LWY4NGEtNDU4Ni05OTgxLTM2MzVhMmNmYTJlMSIsImMiOjE3MTgzNDYxNzYxNjksInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=',
    'autoTriggerLock': '21600',
    's_sq': '%5B%5BB%5D%5D',
    '_ga_Q3470S4J87': 'GS1.1.1718346173.3.1.1718346219.14.0.0',
    '_ga_MGJJ293S48': 'GS1.1.1718346174.3.1.1718346219.15.0.0',
    '_ga_D148XMNPGZ': 'GS1.1.1718346174.3.1.1718346220.0.0.0',
    '_ga_R8B3JV8BYF': 'GS1.1.1718346174.3.1.1718346220.0.0.0',
    '_ga': 'GA1.2.61943451.1718106243',
    'gpv_pn': 'fnp%20ind%3Aplp%3Asaudi-arabia%3Asend%20gifts%20to%20saudi%20arabia',
    'cto_bundle': 'jKtcPF9FSmNsclglMkJzaWN0UU9GV1ZYMVB4cUh5SG5XcWZha1BlRlZmcUxLSmdhcWJTNmxId0VXUHJjcDRvS2ZVemJOSXlIa2hWajVTRHF3VzR1MWtKeWI0M0ZEbDluSzkyWXI4ZTlWQVVFY1RBclFKVGNKeEU5bVBuZGVreHh2NFdTY2dtMDFobHNIbnUzS00zTTE1ZGVmc0lBZk91aGVwdTFaVVZvQklzNVRNYndUb2ZEdFVUYXNUMUpwWFdOMjhNSzB0TUxkRUpaMFJ6RzdNVnBQYmxKQkhvUlZKcGhKenh0eG1yJTJGb1VpenRLYXBoMGVYUmlDb20wOGYwZmVSU2hTJTJCZXRR',
    '_uetsid': '89a789d02a1611efa63fb789a3eb80d6',
    '_uetvid': 'e88c3d5027e711ef979161d15d2ae1e5',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': '_gcl_au=1.1.567078259.1718106242; _fbp=fb.1.1718106243533.999826387763443263; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22Dcs2L15Hm5653wbhLp9U%22%7D; cdp-fngId=d68513ca939bc5ef0617e7ed6a77feb7; cdp-Device-Id=e90d6ca6-27e7-11ef-9e64-f2bcb77acdd0; cdp-mapperId=1; _hjSessionUser_451981=eyJpZCI6ImU0NGYyNTY0LWM1ZjYtNTNjOC1iZTI5LTYzM2JjNmM2YTg2NSIsImNyZWF0ZWQiOjE3MTgxMDYyNDcwMzMsImV4aXN0aW5nIjp0cnVlfQ==; impressionDelayTime=1000; fnp_aton=N; AMCVS_43C357DF589484E40A495D80%40AdobeOrg=1; AMCV_43C357DF589484E40A495D80%40AdobeOrg=179643557%7CMCIDTS%7C19889%7CMCMID%7C52668679803917176142847477469811606077%7CMCAAMLH-1718950972%7C12%7CMCAAMB-1718950972%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1718353372s%7CNONE%7CvVersion%7C5.5.0; localCurrency=INR; _gid=GA1.2.558609106.1718346174; uscnlg=true; s_cc=true; AMO-tid=317833169; usid=1247768968; _hjSession_451981=eyJpZCI6IjFkNmVhZjA2LWY4NGEtNDU4Ni05OTgxLTM2MzVhMmNmYTJlMSIsImMiOjE3MTgzNDYxNzYxNjksInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; autoTriggerLock=21600; s_sq=%5B%5BB%5D%5D; _ga_Q3470S4J87=GS1.1.1718346173.3.1.1718346219.14.0.0; _ga_MGJJ293S48=GS1.1.1718346174.3.1.1718346219.15.0.0; _ga_D148XMNPGZ=GS1.1.1718346174.3.1.1718346220.0.0.0; _ga_R8B3JV8BYF=GS1.1.1718346174.3.1.1718346220.0.0.0; _ga=GA1.2.61943451.1718106243; gpv_pn=fnp%20ind%3Aplp%3Asaudi-arabia%3Asend%20gifts%20to%20saudi%20arabia; cto_bundle=jKtcPF9FSmNsclglMkJzaWN0UU9GV1ZYMVB4cUh5SG5XcWZha1BlRlZmcUxLSmdhcWJTNmxId0VXUHJjcDRvS2ZVemJOSXlIa2hWajVTRHF3VzR1MWtKeWI0M0ZEbDluSzkyWXI4ZTlWQVVFY1RBclFKVGNKeEU5bVBuZGVreHh2NFdTY2dtMDFobHNIbnUzS00zTTE1ZGVmc0lBZk91aGVwdTFaVVZvQklzNVRNYndUb2ZEdFVUYXNUMUpwWFdOMjhNSzB0TUxkRUpaMFJ6RzdNVnBQYmxKQkhvUlZKcGhKenh0eG1yJTJGb1VpenRLYXBoMGVYUmlDb20wOGYwZmVSU2hTJTJCZXRR; _uetsid=89a789d02a1611efa63fb789a3eb80d6; _uetvid=e88c3d5027e711ef979161d15d2ae1e5',
    'if-none-match': '"9d610-Mo7WKOeMWHk2sLDcVZzG736b2CQ"',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
}

params = {
    'promo': 'globalmenu_dt_hm',
}
s.headers.update(headers)

response = requests.get('https://www.fnp.com/saudi-arabia/gifts-lp', params=params, cookies=cookies, headers=headers)

list_all = [ ]

def main_page():
    soup = BS (response.text,"html.parser")
    # category = []
    for i in soup.find("div","sub-navmenubar").find_all("a"):
        links = "https://www.fnp.com" + i.get("href")

    # return category    
        # print(links)
        list_page(links)

def list_page(fnp_links):
    r = s.get(fnp_links)
    # print(r.url)
    soup = BS (r.text,"html.parser")
    # products = [ ]

    for i in soup.find_all("a","product-card_card-container__1oJLc"):
        links = "https://www.fnp.com" + i.get("href")
        # print(links)
        detail_page(links)
    # return products    

def detail_page(fnp_details):
    r = s.get(fnp_details)
    # print(r.url)
    soup = BS (r.text,"html.parser")
    try:
      name = soup.find("h1","price-with-name-desktop_productName__3kv8O").text
    except:
      name = None
    try:    
      price = soup.find("span","odometer odometer-auto-theme").text
    except:
      price = None  
    try:  
      image = soup.find("div","jss7").find("img").get("src")
    except:
      image = None   
    try:
      details = soup.find("div","product-desc-desktop_descriptionTitle__2Q-Ha").find("h4").next.next.text
    except:
      details = None
    try:  
        for i in soup.find("div","product-desc-desktop_descriptionTitle__2Q-Ha").find_all("li"):
            information = (i.text.strip())
    except:
            information = None      
    item = dict()
    item["title"] = name
    item["rate"] = price
    item["photo"] = image
    item["pro_details"] = details
    item['pro_imformation'] = information
    list_all.append(item)
    print(list_all)    
    # print(name)
    # print(price)
    # print(image)
    # print(details)  
    
main_page()    
df = pd.DataFrame(list_all)
df.to_excel("fnp.xlsx")    