import requests
from bs4 import BeautifulSoup

def cvNews():
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

    newsData = []
    newsData.append([title1,link1,content1])
    newsData.append([title2,link2,content2])
    newsData.append([title3,link3,content3])

    return newsData





    # #첫번째 뉴스
    # news1 = total.find("div",attrs={"class":"dbsr"})
    # title1 = news1.find("div",attrs={"class":"JheGif nDgy9d"}).get_text().strip()
    # content1s = news1.find("div", attrs={"class":"Y3v8qd"}).get_text().strip()
    # content1 = content1s[content1s.find(']')+1:]
    # link1 = news1.a["href"]
    # #두번째 뉴스
    # step = total.find_next_sibling("div")
    # news2 = step.find("div",attrs={"class":"dbsr"})
    # title2 = news2.find("div",attrs={"class":"JheGif nDgy9d"}).get_text().strip()
    # content2s = news2.find("div", attrs={"class":"Y3v8qd"}).get_text().strip()
    # content2 = content2s[content2s.find(']')+1:]
    # link2 = news2.a["href"]
    # #세번째 뉴스
    # step2 = step.find_next_sibling("div")
    # news3 = step2.find("div",attrs={"class":"dbsr"})
    # title3 = news3.find("div",attrs={"class":"JheGif nDgy9d"}).get_text().strip()
    # content3s = news3.find("div", attrs={"class":"Y3v8qd"}).get_text().strip()
    # content3 = content3s[content3s.find(']')+1:]
    # link3 = news3.a["href"]
    # #네번째 뉴스
    # step3 = step2.find_next_sibling("div")
    # news4 = step3.find("div",attrs={"class":"dbsr"})
    # title4 = news4.find("div",attrs={"class":"JheGif nDgy9d"}).get_text().strip()
    # content4s = news4.find("div", attrs={"class":"Y3v8qd"}).get_text().strip()
    # content4 = content4s[content3s.find(']')+1:]
    # link4 = news4.a["href"]
    #  #다섯번째 뉴스
    # step4 = step3.find_next_sibling("div")
    # news5 = step4.find("div",attrs={"class":"dbsr"})
    # title5 = news5.find("div",attrs={"class":"JheGif nDgy9d"}).get_text().strip()
    # content5s = news5.find("div", attrs={"class":"Y3v8qd"}).get_text().strip()
    # content5 = content5s[content3s.find(']')+1:]
    # link5 = news5.a["href"]
    #  #여섯번째 뉴스
    # step5 = step4.find_next_sibling("div")
    # news6 = step5.find("div",attrs={"class":"dbsr"})
    # title6 = news6.find("div",attrs={"class":"JheGif nDgy9d"}).get_text().strip()
    # content6s = news6.find("div", attrs={"class":"Y3v8qd"}).get_text().strip()
    # content6 = content6s[content3s.find(']')+1:]
    # link6 = news6.a["href"]