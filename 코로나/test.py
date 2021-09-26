import requests
from bs4 import BeautifulSoup


headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}

url = "https://www.google.co.kr/search?q=%EC%BD%94%EB%A1%9C%EB%82%98+%EB%89%B4%EC%8A%A4&sxsrf=ALeKk03ogE3dQlIdSSRA5y2xi2P2QXjG7g%3A1625495107646&source=hp&ei=QxbjYKvVJMraz7sP2dO4kA4&iflsig=AINFCbYAAAAAYOMkUwvYGtNQ00I9gxMZ2MLEQznDfhlc&oq=%EC%BD%94%EB%A1%9C%EB%82%98+%EB%89%B4%EC%8A%A4&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEMQCMgIIADIHCAAQhwIQFDICCAAyAggAMgIIADIECAAQHjIECAAQHjIECAAQHjIECAAQHjoHCCMQ6gIQJzoECCMQJzoICAAQsQMQgwE6BQgAELEDOg0IABCHAhCxAxCDARAUUJ8OWK8cYKweaARwAHgCgAF6iAHKCJIBAzEuOZgBAKABAaoBB2d3cy13aXqwAQo&sclient=gws-wiz&ved=0ahUKEwjrguSTkczxAhVK7XMBHdkpDuIQ4dUDCAc&uact=5"
res = requests.get(url,headers=headers)
res.raise_for_status()

soap2 = BeautifulSoup(res.text, "lxml")

total = soap2.find("div",attrs={"id":"kp-wp-tab-Latest"}).find("div") #헤드라인 뉴스 전체 가져오기
#첫번째 뉴스
news1 = total.find("a",attrs={"class":"WlydOe"})
title1 = news1.find("div",attrs={"class":"mCBkyc nDgy9d"}).get_text().strip()
content1 = news1.find("div", attrs={"class":"GI74Re nDgy9d"}).get_text().strip()
link1 = news1["href"]

#두번째 뉴스
step = news1.parent.find_next_sibling("div")
news2 = step.find("a",attrs={"class":"WlydOe"})
title2 = news2.find("div",attrs={"class":"mCBkyc nDgy9d"}).get_text().strip()
content2 = news2.find("div", attrs={"class":"GI74Re nDgy9d"}).get_text().strip()
link2 = news2["href"]

#세번째 뉴스
step2 = news2.parent.find_next_sibling("div")
news3 = step2.find("a",attrs={"class":"WlydOe"})
title3 = news3.find("div",attrs={"class":"mCBkyc nDgy9d"}).get_text().strip()
content3 = news3.find("div", attrs={"class":"GI74Re nDgy9d"}).get_text().strip()
link3 = news3["href"]


print(title1)
print(content1)
print(link1)
print(title2)
print(content2)
print(link2)
print(title3)
print(content3)
print(link3)






# newsData = []
# newsData.append([title1,link1,content1])
# newsData.append([title2,link2,content2])
# newsData.append([title3,link3,content3])
# newsData.append([title4,link4,content4])
# newsData.append([title5,link5,content5])
# newsData.append([title6,link6,content6])






