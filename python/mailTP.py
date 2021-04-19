#!/usr/bin/env python
# coding: utf-8

# In[1]:


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

# 쓸일없음 테스트용도
# import getpass
# pw = getpass.getpass()

import pickle  # 패스워드 암호화

# mypass = 'dvckftvywppbltfu'

# save
#with open('pw.pickle', 'wb') as f:
#    pickle.dump(mypass, f, pickle.HIGHEST_PROTOCOL)

# load
with open('pw.pickle', 'rb') as f:
    pwpickle = pickle.load(f)

# userpw = "xxxxxxxxxxx"
smtp_gmail.login(userid, pwpickle)

import pandas as pd
# 저장된 csv 파일 불러오기
emaillist = pd.read_csv("./emailaddress.csv")
# 디버깅용
emaillist

# 만약 컬럼에 공백이 있을경우
# 컬럼을 for문으로 replace로 공백제거 가능
# emailColumns = emaillist.columns
# eamliListOgr = list(emailColumns)
# for i in range(0, len(eamliListOgr)):
#      eamliListOgr[i] = eamliListOgr[i].replace(" ", "")
# emaillist.columns = eamliListOgr
# emaillist

to = emaillist.이메일.tolist()
# 디버깅용
to
# to출력시 나오는 이메일 값을 복사
to = ["seunghyun7272@gmail.com", "zmxnc10@naver.com"]

# 이메일 주소정보 리스트 변환
emaillist.이메일.tolist()

msg=EmailMessage()
# 제목 입력
msg['Subject']="퀴즈 정보"
# 내용 입력
msg.set_content("퀴즈정보")
# 보내는 사람
msg['From']='seunghyun7272@gmail.com'
# 받는 사람
msg['To'] = ",".join(to)

# 첨부파일 #1 추가
file='json_xml.ipynb'

fp = open(file,'rb')
file_data=fp.read()

msg.add_attachment(file_data,
                    maintype='text',
                    subtype='plain',
                    filename=file)
# 첨부파일 #2 추가
file2='scrapy.ipynb'

fp = open(file,'rb')
file_data=fp.read()

msg.add_attachment(file_data,
                    maintype='text',
                    subtype='plain',
                    filename=file2)

# 메일 전송
smtp_gmail.send_message(msg)
smtp_gmail.close()

