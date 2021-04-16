#!/usr/bin/env python
# coding: utf-8

# #### 자신이 원하는 쇼핑물 사이트에서 검색한 제품의 제품명 및 가격정보를 수집하세요.

# In[ ]:


import requests, bs4
import pandas as pd

targetUrl = "https://www.coupang.com/np/categories/449593"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:71.0) Gecko/20100101 Firefox/71.0'}
data = requests.get(targetUrl,headers=headers)
bs = bs4.BeautifulSoup(data.text, 'html.parser')

dataTag = bs.find("ul", {"id":"productList"})

nameTag = dataTag.find_all("div", {"class":"name"})

priceTag = dataTag.find_all("strong", {"class":"price-value"})

nameList = []
priceList = []

nameList = nameTag[0].text

priceList = priceTag[0].text

rowList = []

for i in range(0, len(nameTag)):
    nameList = nameTag[i].text
    priceList = priceTag[i].text
    totalList = [nameList, priceList] 
    rowList.append(totalList)
totalList = []

pd.DataFrame(rowList, columns=["상품", "가격(원)"])


# ### 2

# In[ ]:


# 라이브러리 선언
import requests, bs4
import pandas as pd
# Url 불러오기 headers 우회(맥 일반 사용자 인식)
targetUrl = "https://www.coupang.com/np/categories/449593"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:71.0) Gecko/20100101 Firefox/71.0'}
data = requests.get(targetUrl,headers=headers)
# parser를 통해 깔끔하게 보이게 함
bs = bs4.BeautifulSoup(data.text, 'html.parser')
# ul > div, strong 에서 name, price를 따로 변수지정
dataTag = bs.find("ul", {"id":"productList"})
nameTag = dataTag.find_all("div", {"class":"name"})
priceTag = dataTag.find_all("strong", {"class":"price-value"})
# List 초기화
rowList = []
nameList = []
priceList = []

for i in range(0, len(nameTag)):
    nameList = nameTag[i].text
    priceList = priceTag[i].text
    rowList.append([nameList, priceList])

product = pd.DataFrame(rowList, columns=["상품", "가격(원)"])
# 상품 1개 출력
product.head(1)


# #### TIMEANDDATETIME내 SOUTHKOREA 연휴 정보 또는 자신이 원하는 테이블 정보를 수집하세요.

# In[ ]:


# 라이브러리 선언
import requests, bs4
import pandas as pd
# Url 불러오기
resp = requests.get("https://www.timeanddate.com/holidays/south-korea/")
resp.encoding='utf-8'
html = resp.text
# parser를 이용해 정리
bs = bs4.BeautifulSoup(html, 'html.parser')

tableTag = bs.find("table", {"id":"holidays-table"})
tbodyTag = tableTag.find(name = "tbody")
trs = tbodyTag.find_all(name = "tr")

# trs의 [0]은 빈 값
dateTag = trs[1].find_all(name = ["th", "td"])
# 디버깅용

# List 초기화
rowList = []
dateList = []
# for문 사용
for i in range(0, len(trs)):
    dateTag = trs[i].find_all(name = ["th", "td"])
    # trs[0],[7]~~의 값은 비어있기 때문에 if을 이용 continue로 스킵
    if dateTag == []:
        continue
    for j in range(0, len(dateTag)):
        # dateTag[2]의 값은 링크가 같이 나오기 때문에 text로 사용해야 함
        dateList.append(dateTag[j].text)
    rowList.append(dateList)
    dateList = []
# DataFrame을 만들고 columns를 따로 지정(Day:요일 부분은 값이 없음, 3중이 힘듦)
hoilday = pd.DataFrame(rowList, columns=["Date", "Day", "Name", "Type"])
hoilday


# ### 2

# In[ ]:


# 라이브러리 선언
import requests, bs4
import pandas as pd
# Url 불러오기
resp = requests.get("https://www.timeanddate.com/holidays/south-korea/")
resp.encoding='utf-8'
html = resp.text
# parser를 이용해 정리
bs = bs4.BeautifulSoup(html, 'html.parser')
# table > tbody > tr > th, td
tableTag = bs.find("table", {"id":"holidays-table"})

tbodyTag = tableTag.find("tbody")

trTag = tbodyTag.find_all("tr")

dateTag = trTag[1].find_all(["th", "td"])

dateTag

# List 초기화
rowList = []
dateList = []

# for문 사용
for i in range(0, len(trTag)):
    dateTag = trTag[i].find_all(name = ["th", "td"])
    # trs[0],[7]~~의 값은 비어있기 때문에 if을 이용 continue로 스킵
    if dateTag == []:
        continue
    for j in range(0, len(dateTag)):
        # dateTag[2]의 값은 링크가 같이 나오기 때문에 text로 사용해야 함
        dateList.append(dateTag[j].text)
    rowList.append(dateList)
    dateList = []
    
# DataFrame을 만들고 columns를 따로 지정(page에 컬럼 Day:요일 부분은 값이 없음)
hoilday = pd.DataFrame(rowList, columns=["Date", "Day", "Name", "Type"])
hoilday

