#!/usr/bin/env python
# coding: utf-8

# ##### [데이터타입 통합]
# ##### kopo_channel_seasonality_new.csv 파일을 불러온 후
# ##### selloutData 변수에 담으세요 이후
# ##### QTY컬럼→실수(float), 이외컬럼→문자(str)로 변경하세요

# In[1]:


# 라이브러리 선언
import pandas as pd
import numpy as np

# csv 파일 데이터 불러오기
selloutData = pd.read_csv("../dataset/kopo_channel_seasonality_new.csv")
# selloutData.describe() # 기본통계량을 알려줌

# selloutData의 type확인
selloutData.dtypes
# YEARWEEK컬럼의 int를 str로 변환
selloutType = selloutData.astype({"YEARWEEK":str})
# selloutData에 selloutType를 담아줌
selloutData = selloutType
# selloutData의 type확인
selloutData.dtypes
# head() 상위 5개만 출력
# selloutData.head()


# ##### [데이터타입 조회]
# ##### kopo_customerdata.csv 파일을 불러온 후
# ##### kopo_customerData 변수에 담으세요 이후
# ##### STATENAME, GENDER 컬럼 첫 5개행 조회하세요

# In[2]:


# 라이브러리 선언
import pandas as pd
# csv 파일 불러오기
customerData = pd.read_csv("../dataset/kopo_customerdata.csv")
# 컬럼명 변수 지정
targetColumns = ["STATENAME","GENDER"]
# customerData 안의 targetColumns 컬럼을 조회
customerDataC = customerData.loc[:, targetColumns]
# head()로 5개행 조회
# customerDataC.head()


# # 프로젝트 실습
#  [불량 데이터 처리]
#  kopo_channel_seasonality_new.csv 자료를 담은
#  selloutData 변수에서
#  
#  QTY컬럼 음수(반품)인 경우 0, 양수인 경우 기존 QTY 값
#  유지하는 로직을 적용하여 QTY_NEW 컬럼을 추가하세요

# In[1]:


# 라이브러리 선언
import pandas as pd
import numpy as np
# csv 파일 불러오기 (selloutData 변수에 담아줌)
selloutData = pd.read_csv("../dataset/kopo_channel_seasonality_new.csv")
# 함수 사용
def valueQTY(inValue):
    # inValue = -1 디버깅용
    outValue = inValue

    if inValue < 0:
        outValue = 0
    else:
         pass
    return outValue
# selloutData 테이블에 새로운 QTY_NEW생성 QTY에 함수를 적용시킴
selloutData["QTY_NEW"] = selloutData.QTY.apply(valueQTY)
# head() 상위 5개만 출력
# selloutData


# [데이터 통합]
# selloutData 자료에서
# YEAR, WEEK 컬럼을 생성하고 WEEK 가 52 이하인
# 데이터만 조회한 후 refinedSelloutData 변수에 담으세요
# 

# In[2]:


# selloutData의 dtype 확인
# selloutData.info()

# YEARWEEK (int -> str) 형변환
selloutType = selloutData.astype({"YEARWEEK":str})
selloutData = selloutType

# YEAR / WEEK 로 나누어 새로운 컬럼 생성
selloutData["YEAR"] = selloutData.YEARWEEK.str[0:4]
selloutData["WEEK"] = selloutData.YEARWEEK.str[4:8]
# 출력 확인용
# selloutData.head()

# selloutData의 dtype 확인
# selloutData.info()

# str형태인 WEEK를 int형태로 변환하고 52보다 작은 수만 조회
refinedSelloutData = selloutData[selloutData.WEEK.astype(int) <= 52]
# 출력 확인용
# refinedSelloutData

# 53주차를 제외한 len 확인
# len(selloutData)
# len(refinedSelloutData)


# refinedSelloutData 에서 →
# 지역, 상품, 연주차 컬럼순으로 오름차순 정렬하여
# sortedData 변수에 담으세요

# In[3]:


# 지역, 상품, 연주차를 정렬하기 위해 sortKey에 담아둠
sortKey = ["REGIONID","PRODUCT","YEARWEEK"]
# refinedSelloutData데이터를 정렬 함수를 이용해 ascending(오름차순) 정렬[O,O,O], 즉시 적용(X), 아무 인덱스 - 무시하라
sortedData = refinedSelloutData.sort_values(by=sortKey, ascending=[True,True,True], inplace=False, ignore_index=True)


# [지역, 상품, 연도 별 집계]
# sortedData 에서 지역, 상품, 연도 단위
# 판매량(QTY_NEW) 의 평균 연산 후
# groupData 변수에 담으세요
# 
# 이후 컬럼명을 QTY_MEAN로 변경하세요
# 

# In[4]:


# group를 하기 위한 지역, 상품, 연도
groupKey = ["REGIONID","PRODUCT","YEAR"]
# groupKey에 담긴 지역, 상품, 연도와 QTY_NEW의 평균 연산을 인덱스를 초기화 후에 groupData에 담아줌
groupData = sortedData.groupby(by=groupKey)["QTY_NEW"].agg("mean").reset_index()
# sortedData의 컬럼을 재정의 (기존 컬럼명 : 바꿀 컬럼명)
groupData = groupData.rename(columns = {"QTY_NEW":"QTY_MEAN"})
# 출력 확인용
# groupData.head(4)


# refinedSelloutData와 groupData를
# [REGIONID, PRODUCT, YEAR] 키로 조인하여
# mergedData 변수에 아래와 같이 담으세요

# In[5]:


import numpy as np

# join을 하기 위한 Key
joinKey = ["REGIONID", "PRODUCT", "YEAR"]

# refinedSelloutData를 기준으로 left 조인
mergedData = pd.merge(left=refinedSelloutData,
                      right=groupData,
                      left_on = joinKey,
                      right_on = joinKey,
                      how = "left"
                      )

mergeSortKey = ["REGIONID", "PRODUCT", "YEARWEEK"]
# refinedSelloutData데이터를 정렬 함수를 이용해 ascending(오름차순) 정렬[O,O,O], 즉시 적용(X), 아무 인덱스 - 무시하라
mergedData = mergedData.sort_values(by=mergeSortKey, ascending=[True,True,True], inplace=False, ignore_index=True)

# mergedData


# 계절성 지수는
# QTY_NEW / QTY_MEAN
# 으로 산출하여 SEASONALITY 컬럼을 생성한다

# In[6]:


mergedData["SEASONALITY"] = mergedData.QTY_NEW / mergedData.QTY_MEAN


# ## 결과값

# 마지막으로 [지역, 상품, 주차] 별
# 계절성 지수 평균 값을
# 산출하여 finalResult 변수에 담으세요

# In[7]:


# group를 하기 위한 지역, 상품, 주차
groupKey = ["REGIONID","PRODUCT","WEEK"]
# groupKey에 담긴 지역, 상품, 주차 SEASONALITY의 평균 연산을 인덱스를 초기화 후에 finalResult 담아줌
finalResult = mergedData.groupby(by=groupKey)["SEASONALITY"].agg("mean").reset_index()


# In[8]:


finalResult


# #### ---------------------------------------------------------------------------------------------------------------------------------------------------

# # 단계별

# 추세선 (구간 = 13)

# In[9]:


mergedData["TrendLine"] = mergedData.QTY_NEW.rolling(window=13, min_periods=1, center=True).mean()


# 변동률 (구간=5, 추세선기준)

# In[10]:


mergedData["RateOfChange"] = mergedData.TrendLine.rolling(window=5, min_periods=1, center=True).mean()


# 상한선 (추세선+변동률) / 하한선 (추세선-변동률)

# In[11]:


upperLimit = mergedData.TrendLine + mergedData.RateOfChange # 상한선
lowerLimit = mergedData.TrendLine - mergedData.RateOfChange # 하한선
ulLimit = zip(upperLimit,lowerLimit)
uplowList = pd.DataFrame(ulLimit, columns=["upperLimit","lowerLimit"])
# 기존의 데이터와 uplowList를 옆으로 붙임
mergedData = pd.concat( [mergedData, uplowList], axis=1)


# 정제된 판매량
# (실제판매량>상한선-> 상한선
#  실제거래량<하한선-> 하한선
# 이외에는 실제판매량을 유지

# In[12]:


def refining(mergedData):
    if mergedData['QTY_NEW'] > mergedData['upperLimit']:
        return mergedData['upperLimit']
    elif mergedData['QTY_NEW'] < mergedData['lowerLimit']:
        return mergedData['lowerLimit']
    else:
        return mergedData['QTY_NEW']


# In[13]:


mergedData["RefinedSales"]=mergedData.apply(refining, axis=1)


# 최종 추세선 (구간=5)

# In[14]:


mergedData["FinalLine"] = mergedData.RefinedSales.rolling(window=5, min_periods=1, center=True).mean()
# mergedData

# mergedData.FinalLine.isnull().sum()


# 안정된 시장의
# 계절성 지수
# =실제판매량/최종 추세선

# In[15]:


mergedData["stSeasonality"] = mergedData["QTY_NEW"] / mergedData["FinalLine"]


# In[16]:


# nan값 확인
# mergedData.stSeasonality.isnull().sum()
# mergedData.QTY_NEW.isnull().sum()


# 불안정 시장의
# 계절성 지수
# =정제된판매량/최종추세선

# In[17]:


mergedData["itSeasonality"] = mergedData["RefinedSales"] / mergedData["FinalLine"]


# In[18]:


import numpy as np
mergedData.isnull().sum()
mergedData.dropna(how='all') # nan 포함하는 행 삭제
mergedData


# In[19]:


import warnings
warnings.filterwarnings(action='ignore')
# group를 하기 위한 지역, 상품, 주차
groupKey = ["REGIONID","PRODUCT","WEEK"]
# groupKey에 담긴 지역, 상품, 연도와 계절성 지수(안정시장, 불안정 시장)의 평균 연산을 인덱스를 초기화 후에 finalResult 담아줌
finalResult = mergedData.groupby(by=groupKey)["stSeasonality", "itSeasonality"].agg("mean").reset_index()
finalResult


# In[21]:


# finalResult.describe()

