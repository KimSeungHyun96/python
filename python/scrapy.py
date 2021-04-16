#!/usr/bin/env python
# coding: utf-8

# ### 0. Pandas 데이터프레임

# In[ ]:


import pandas as pd


# ### 0-1. 리스트에서 데이터프레임 생성

# In[ ]:


rowFirst = ["A01", 202015, 100]
rowSecond = ["A01", 202016, 100]
rowThird = ["A01", 202017, 100]


# In[ ]:


df1 = pd.DataFrame( [rowFirst, rowSecond, rowThird] )


# In[ ]:


df1.columns = ["REGIONID", "YEARWEEK, "QTY"]


# In[ ]:


columnNameList = ["regionid", "yearweek", "qty"]


# In[ ]:


df1


# In[ ]:


columnFirst = ["A0", "A01", "A01"]
columnSecond = [202015,202016,202017]
columnThird = [100,110,150]


# In[ ]:


pd.DataFrame( (zip(columnFirst, columnSecond, columnThird)))


# In[ ]:


pd.DataFrame( (zip(columnFirst, columnSecond, columnThird) )


# In[ ]:


df2.columns = columnNameList


# In[ ]:


df2


# ### 1. 라이브러리 선언

# In[1]:


from bs4 import BeautifulSoup
import requests


# ### 2. 타겟 URL 선언 및 접속

# In[2]:


targetUrl = "http://www.sparkkorea.com/퀴즈"

resp = requests.get(url=targetUrl)

resp.encoding = "utf-8"

##### 원 소스전부 스크랩

html = resp.text

##### 데이터 정제 html.parse

htmlObj = BeautifulSoup(html, "html.parser")

### 3. 태그 값 접근

htmlObj.findAll(name="a")

##### find > 계속 범위를 좁히기 / findAll을 활용 반복해서 수집

targetParent = htmlObj.find(name="div", attrs = {"id":"id_spark_quiz"})

valueList = []

atags = targetParent.findAll(name="a")


# In[ ]:


# 1
#eachTag = atags[0]
#valueList.append(tagText)
#valueList


# In[8]:


eachTag = targetParent.find(name="a")


# In[9]:


eachTag.name
eachTag.text


# In[21]:


for i in range(0, len(atags)):
    #각 태그정보 수집
    eachTag = atags[i]
    tagText = eachTag.text
    valueList.append(tagText)


# In[14]:


link = eachTag.attrs["href"]


# In[15]:


link


# In[16]:


linkTag = link[i]


# In[19]:


linkList = []


# In[20]:


linkList.append(linkTag)


# In[11]:


# 리스트에 태그내 text 정보 append
valueList


# ##### a태그에는 href라는 속성이 있고 href 속성의 값은 https://... => div 태그가 있고 id라는 속성에 id_spark_quiz

# In[1]:


from bs4 import BeautifulSoup
import requests

targetUrl = "http://www.sparkkorea.com/퀴즈"
resp = requests.get(url=targetUrl)
resp.encoding = "utf-8"

html = resp.text
htmlObj = BeautifulSoup(html, "html.parser")
htmlObj.findAll(name="a")

targetParent = htmlObj.find(name="div", attrs = {"id":"id_spark_quiz"})

atags = targetParent.findAll(name="a")

eachTag = targetParent.find(name="a")

rowList = []
columnList = []

columnList.append(eachTag.text)
columnList.append(eachTag.name)
columnList.append(eachTag.attrs["href"])

for i in range(0, len(atags)):
    eachTag = atags[i].findAll(name="a")
    for j in range(0, len(eachTag)):
        if i ==0:
            columnNameList.append(eachTag[i].name)
        eachColumn = eachTag[j].text
        columnList.append(eachColumn)
    rowList.append(columnList)

    columnList = []

# 리스트에 태그내 text 정보 append
rowList


# In[ ]:


from bs4 import BeautifulSoup
import requests

targetUrl = "http://www.sparkkorea.com/퀴즈"
resp = requests.get(url=targetUrl)
resp.encoding = "utf-8"

html = resp.text
htmlObj = BeautifulSoup(html, "html.parser")
htmlObj.findAll(name="a")

targetParent = htmlObj.find(name="div", attrs = {"id":"id_spark_quiz"})

atags = targetParent.findAll(name="a")

eachTag = targetParent.find(name="a")


# In[1]:


import requests, bs4
import pandas as pd

resp = requests.get("https://sparkkorea.com/테스트/")
resp.encoding='utf-8'
html = resp.text
bs = bs4.BeautifulSoup(html, 'html.parser')

tabletag = bs.find("table", {"id":"test_table"})

tbodyTag = tabletag.find("tbody")

trs = tbodyTag.findAll("tr")

eachTrs = trs[0]

tds = eachTrs.findAll("td")

rowList = []
columnList = []

for i in range(0,len(trs)):
    eachTrs = trs[i]
    tds = eachTrs.findAll("td")
    for j in range(0,len(tds)):
        eachTd = tds[j]
        columnList.append(eachTd.text)
    rowList.append(columnList)
    columnList = []

rowList


# In[3]:


import requests, bs4
import pandas as pd

resp = requests.get("https://sparkkorea.com/테스트/")
resp.encoding='utf-8'
html = resp.text
bs = bs4.BeautifulSoup(html, 'html.parser')

tabletag = bs.find("table", {"id":"test_table"})
rows = tabletag.find("tbody").findAll("tr")

rowList=[]
columnList =[]

for i in range(0, len(rows)):
    columns = rows[i].findAll("td")
    columnsLen = len(columns)
    for j in range(0, columnsLen):
        columnList.append(columns[j].text)

    rowList.append(columnList)
    columnList=[]

rowList

pd.DataFrame(rowList, columns =["학번","이름"])

