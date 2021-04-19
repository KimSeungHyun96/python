#!/usr/bin/env python
# coding: utf-8

# #### 셀레니움을 활용 sparkkorea.com quiz에 접근
# #### 이후 spark 관련 퀴즈 타이틀과 링크정보를 수집하여 데이터프레임으로 변환

# In[1]:


# 라이브러리 선언
import pandas as pd
from selenium import webdriver

# 웹브라우저 설정
options = webdriver.ChromeOptions()
driverLoc = "../addon/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=driverLoc, options=options)
options.add_argument("window-size=1920x1080")

# 브라우저 열기
targetUrl = "https://www.sparkkorea.com"
driver.get(targetUrl)

# 브라우저 설정
quizBtnXpath = '//*[@id="menu-item-382"]'
# 큰창에서만 클릭가능 (*중요*)
quizBtn = driver.find_element_by_xpath(quizBtnXpath).click()

# 라이브러리 선언
import requests, bs4
# 페이지 URL Source 가져오기
driver.current_url
driver.page_source

resp = driver.current_url
# 주소 가져오기 (resp = driver.current_url)
resp = requests.get("https://sparkkorea.com/%ed%80%b4%ec%a6%88/")
resp.encoding='utf-8'
html = resp.text
# parser를 이용해 정리
bs = bs4.BeautifulSoup(html, 'html.parser')

# 테이블 정보 수집
tableTag = bs.find("article", {"id":"post-102"})
quizTag = tableTag.find("div", {"id":"id_spark_quiz"})
quiz = quizTag.find_all("a")

# column = quizTag.find_all("h1")

# List 초기화
rowList = []
columnList = []
# for문 사용 (text와 link를 배열에 넣어줌)
for i in range(0,len(quiz)):
    columnList.append(quiz[i].text)
    rowList.append(quiz[i].attrs["href"])
answer = pd.DataFrame( zip (columnList, rowList) )
# 컬럼명 설정
answer.columns = ["Spark 퀴즈", "link"]

answer

