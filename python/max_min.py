#!/usr/bin/env python
# coding: utf-8

# ### csv파일을 불러오고 max,min의 값의 합과 평균을 구함

# In[13]:


# 라이브러리 선언
import pandas as pd
# csv파일 읽어오기
customerData = pd.read_csv("../SMART-06/dataset/kopo_customerdata.csv")
# TOTAL_AMOUNT를 통해 열 형해로 보이게 함
customerTotalList = customerData["TOTAL_AMOUNT"].tolist()
# customerTotalList 정렬
customerTotalList.sort()
# max, min의 값을 카운트해서 List에 넣어줌
customerMaxList = customerTotalList.count(max(customerTotalList))
customerMinList = customerTotalList.count(min(customerTotalList))

maxlist = max(customerTotalList)
minlist = min(customerTotalList)
# maxlist 삭제 , del의 방법으로 minList 삭제
customerTotalList.remove(maxlist)
del customerTotalList[:customerMinList]
# sum / len으로 평균도출
average = sum( (customerTotalList)) / len( (customerTotalList))

average
# del customerTotalList[customerMaxList]
# del customerTotalList[customerMinList]

# average = sum( (customerTotalList)) / len( (customerTotalList))

# average

