#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 라이브러리
import pandas as pd
# 공공데이터 파일 불러오기
LoanUrl = "url"
json = pd.DataFrame() 
# 예외처리
try:
    json = pd.read_json(LoanUrl)
except Exception as e:
    print(e)
# json 앞 5개 출력
json.head(5)


# In[ ]:


import pandas as pd
# 82500원 2008년도
# 72500원 2010년도
rowList = []
columnList = []
columnList.append("82500")
columnList.append("2008")
rowList.append(columnList)
# columnList를 초기화 시키고 다른 정보 추가
# rowList는 초기화 시키지 않음
columnList = []
columnList.append("72500")
columnList.append("2010")
rowList.append(columnList)
rowList
pd.DataFrame(rowList)


# In[ ]:


import requests
from lxml import html
from bs4 import BeautifulSoup 
import pandas as pd
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote

API_Key = unquote('AT33s775KYpJOkUBJu0dxkJuUeIfDIOJRzAH084EQS3JN%2BzFjErLHuk%2FGZa9L4gBTSGCzeA69tI9PwLp7B37IQ%3D%3D')
url = "http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev"

queryParams = '?' + urlencode(
    {quote_plus('ServiceKey') : API_Key,
     quote_plus('LAWD_CD'): '11110',
     quote_plus('DEAL_YMD'): '201512'
    }
)

response = requests.get(url+queryParams)
response.encoding='utf-8'

xmlobj = BeautifulSoup(response.text,"lxml-xml")

rows = xmlobj.find_all('item')
# 디버깅용
rows[0]

columns = rows[0].find_all()
# 디버깅용
columns
# columns name, text 확인
columns[0].name
columns[0].text

# 초기화
rowList = []
columnList = []
columnNameList = []

for i in range(0, len(rows)):
    columns = rows[i].find_all()
    for j in range(0, len(columns)):
        if i == 0:
            columnNameList.append(columns[j].name)
        eachColumn = columns[j].text
        columnList.append(eachColumn)
    rowList.append(columnList)
    columnList = []

indata = pd.DataFrame(rowList, columns=columnNameList)

indata


# In[ ]:


import requests
from lxml import html
from bs4 import BeautifulSoup 
import pandas as pd
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote

response = requests.get("http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev?serviceKey=AT33s775KYpJOkUBJu0dxkJuUeIfDIOJRzAH084EQS3JN%2BzFjErLHuk%2FGZa9L4gBTSGCzeA69tI9PwLp7B37IQ%3D%3D&pageNo=1&numOfRows=10&LAWD_CD=11110&DEAL_YMD=201512")
response.encoding='utf-8'

xmlobj = BeautifulSoup(response.text,"lxml-xml")

rows = xmlobj.find_all('item')


columns = rows[0].find_all()
# 디버깅용
columns
# columns name, text 확인
columns[0].name
columns[0].text


# In[ ]:


# 초기화
rowList = []
columnList = []
columnNameList = []

for i in range(0, len(rows)):
    columns = rows[i].find_all()
    for j in range(0, len(columns)):
        if i == 0:
            columnNameList.append(columns[j].name)
        eachColumn = columns[j].text
        columnList.append(eachColumn)
    rowList.append(columnList)
    columnList = []

indata = pd.DataFrame(rowList, columns=columnNameList)

indata

