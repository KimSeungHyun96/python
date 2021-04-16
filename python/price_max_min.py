#!/usr/bin/env python
# coding: utf-8

# ### custmoerdata amount_price 최소 최대값을 뺀 평균을 구한다.

# In[3]:


import pandas as pd

csData = pd.read_csv("../dataset/kopo_customerdata.csv")

amountList = csData.TOTAL_AMOUNT.tolist()

amountList.sort()


# ##### Step1: 데이터를 정렬한다. (오름차순)

# In[7]:


amountList.sort()


# ##### Step2: 최소값 최대값을 계산한다.

# In[8]:


minValue = amountList[0]
maxValue = amountList[-1]


# In[9]:


minValue = min(amountList)
maxValue = max(amountList)


# ##### Step3: 최소값 최대값 각각의 개수를 산출한다.

# In[10]:


minValueCnt = amountList.count(minValue)
maxValueCnt = amountList.count(maxValue)


# ##### Step4: 평균계산
# 

# ##### 초기리스트합 - (최소값 * 최소값개수) - (최대값 * 최대값개수) 
# ##### / 초기리스트개수 - (최소값개수) - (최대값 개수)

# In[17]:


finalSum = sum(amountList) - (minValue*minValueCnt) - (maxValue*maxValueCnt) 

finalLen = (len(amountList)) - (minValueCnt) - (maxValueCnt)

answer = finalSum / finalLen

answer

