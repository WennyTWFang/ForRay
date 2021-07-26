#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://cn.investing.com/equities/apple-computer-inc-historical-data"
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.text, 'html.parser')

html = soup.find(id = "curr_table").tbody
y = html.text
list1 = y.split("\n\n")
result = {}
for i in list1[1:-1]:
    a = i.split("\n")
    if a[0] == "":
        v = a[6].split("M")
        result.update({a[1]:{"close": a[2], "open": a[3], "high": a[4], "low": a[5], "vol": v[0]+"M", "range":v[1]}})
    else:
        v = a[5].split("M")
        result.update({a[0]:{"close": a[1], "open": a[2], "high": a[3], "low": a[4], "vol": v[0]+"M", "range":v[1]}})
print(result)
# import re
# list1 = html.split("<tr>\n<td class=\"first left bold noWrap\" data-real-value=")
# dict_result = [];day2 = [];prise2 = [];volume2=[];percent2=[];
# for i in range(0,len(list1)):
#     if list1[i] != []:
#         day = re.findall("\d+年\d+月\d+日",list1[i])
#         for j in day:
#             if j !=[]:
#                 day2.append(j)
#         prise = re.findall("data-real-value=\"\d\d\d.\d\d\"",list1[i])
#         for k in prise:
#             if k != []:
#                 prise2.append(k.replace('data-real-value=', "").replace('"', ""))
#         volume = re.findall(">.*M",list1[i])
#         for a in volume:
#             if a != []:
#                 volume2.append(a.replace(">",""))
#         percent = re.findall(">-*\d+.\d+%",list1[i])
#         for b in percent:
#             if b != []:
#                 percent2.append(a.replace(">",""))
#         dict_result.append([day,[prise, volume, percent]])
# print(dict_result)
# open_prise = re.findall("\d+年\d+月\d+日",text)
# high = re.findall("\d+年\d+月\d+日",text)
# low = re.findall("\d+年\d+月\d+日",text)
# range_prise = re.findall("\d+年\d+月\d+日",text)
# print(list1)
# df = pd.read_html(str(html), header = 0)[0]

# print(df)
# headers = {
# :authority: cn.investing.com
# :method: GET
# :path: /equities/apple-computer-inc-historical-data
# :scheme: https
# accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
# accept-encoding: gzip, deflate, br
# accept-language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7
# cache-control: max-age=0
# cookie: logglytrackingsession=b49ea460-d00e-4b2b-b5e7-1ba8a3b303cc; PHPSESSID=lt5c0u20d1iic8pc7eqt8qar5m; SideBlockUser=a%3A2%3A%7Bs%3A10%3A%22stack_size%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Bi%3A8%3B%7Ds%3A6%3A%22stacks%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Ba%3A1%3A%7Bi%3A0%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A4%3A%226408%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A28%3A%22%2Fequities%2Fapple-computer-inc%22%3B%7D%7D%7D%7D; geoC=TW; adBlockerNewUserDomains=1627291318; StickySession=id.23059254203.989cn.investing.com; udid=dc7448f5c99e96dba1149af65bb0126f; __cflb=0H28uxmf5JNxjDUC6WDvQUEoJyvKUTqwPn61uSCp1dv; __gads=ID=4b4eb919e3648788:T=1627291320:S=ALNI_MYFqYUhnjzax1FSqSIT5TTdE5T-Kw; protectedMedia=2; _ga=GA1.2.1528658918.1627291320; _gid=GA1.2.1008979733.1627291323; G_ENABLED_IDPS=google; adsFreeSalePopUp=3; Hm_lvt_a1e3d50107c2a0e021d734fe76f85914=1627291324,1627291532,1627299698,1627304916; Hm_lpvt_a1e3d50107c2a0e021d734fe76f85914=1627304916; smd=dc7448f5c99e96dba1149af65bb0126f-1627309473; _gat_allSitesTracker=1
# sec-ch-ua: " Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"
# sec-ch-ua-mobile: ?0
# sec-fetch-dest: document
# sec-fetch-mode: navigate
# sec-fetch-site: cross-site
# sec-fetch-user: ?1
# upgrade-insecure-requests: 1
# user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36
# }
