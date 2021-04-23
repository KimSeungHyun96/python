#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 라이브러리 선언
import pandas as pd
from selenium import webdriver

# 웹브라우저 설정
options = webdriver.ChromeOptions()
driverLoc = "../addon/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=driverLoc, options=options)
options.add_argument("window-size=1920x1080")

# 브라우저 열기
targetUrl = "http://www.coor.kr/"
driver.get(targetUrl)

# 브라우저 설정 (카테고리 store)
storeBtnXpath = '//*[@id="aside"]/ul/li[2]/a' 
quizBtn = driver.find_element_by_xpath(storeBtnXpath).click()

# 브라우저 설정 (카테고리 T-shirt)
tshirtBtnXpath = '//*[@id="aside"]/ul/li[8]/a' 
quizBtn = driver.find_element_by_xpath(tshirtBtnXpath).click()

# 라이브러리 선언
import requests, bs4
# 페이지 URL Source 가져오기
driver.current_url
driver.page_source

resp = driver.current_url
# 주소 가져오기 (resp = driver.current_url)
resp = requests.get("http://www.coor.kr/shop/shopbrand.html?xcode=009&amp;type=X&amp;mcode=005")
resp.encoding='ms949'
html = resp.text
# parser를 이용해 정리
bs = bs4.BeautifulSoup(html, 'html.parser')

itemTag = bs.find("div", {"class":"listItem"})

item = itemTag.find_all("p")

price = itemTag.find_all("li", {"class":"price3"})

nameList = []
priceList = []

nameList = item[0].text

priceLsit = price[0].text

rowList = []
columnList = []

for i in range(0,len(item)):
    nameList = item[i].text.replace("\n", "")
    priceLsit = price[i].text
    columnList = [nameList, priceLsit]
    rowList.append(columnList)
columnList = []

product = pd.DataFrame(rowList, columns=["상품", "가격(원)"])
product


# In[13]:


import smtplib
from email.message import EmailMessage

# GMAIL 메일 설정
smtp_gmail = smtplib.SMTP('smtp.gmail.com', 587)
# 서버 연결을 설정하는 단계
smtp_gmail.ehlo()
# 연결을 암호화
smtp_gmail.starttls()
#로그인
userid = "seunghyun7272"

import pickle  # 패스워드 암호화

# load
with open('pw.pickle', 'rb') as f:
    pwpickle = pickle.load(f)

smtp_gmail.login(userid, pwpickle)

import pandas as pd
# 저장된 csv 파일 불러오기
emaillist = pd.read_csv("./email.txt")
# 디버깅용
emaillist

# 이메일 주소정보 리스트 변환
to = emaillist.이메일.tolist()
# 디버깅용
to
# to출력시 나오는 이메일 값을 복사
to = ["seunghyun7272@gmail.com", "zmxnc10@naver.com"]

msg=EmailMessage()
# 제목 입력
msg['Subject']="셀레니움 자동화"
# 내용 입력
msg.set_content("셀레니움_웹크롤링")
# 보내는 사람
msg['From']='seunghyun7272@gmail.com'
# 받는 사람
msg['To'] = ",".join(to)

# 첨부파일 #1 추가
file='selenium_mailTP.ipynb'

fp = open(file,'rb')
file_data=fp.read()

msg.add_attachment(file_data,
                    maintype='text',
                    subtype='plain',
                    filename=file)

smtp_gmail.send_message(msg)
smtp_gmail.close()

