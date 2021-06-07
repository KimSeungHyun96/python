#!/usr/bin/env python
# coding: utf-8

# ### 라이브러리 정의

# In[2]:


# 데이터 처리 라이브러리
import pandas as pd
import numpy as np
# 분석알고리즘 DecisionTree 구현 라이브러리
from sklearn.tree import DecisionTreeRegressor # 설명도가 높아짐
# 과거데이터를 8:2, 7:3 이나 이런식으로 자동으로 나누어주는 라이브러리
from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestRegressor  # 설명은 낮지만 정확도가 높아짐
from sklearn.linear_model import LinearRegression # YES or NO

from sklearn.preprocessing import LabelEncoder  # 숫자로 만들어주는..
# 분석 Regression 평가 대표 지표 (MAE, RMSE)
from sklearn.metrics import mean_absolute_error # MAE
from sklearn.metrics import mean_squared_error # RMSE


# ### 데이터 불러오기

# In[3]:


featuresData = pd.read_csv("../dataset/feature_regression_example.csv")
featuresData.head(2)


# ### 1. 데이터 전처리

# ### 1-1. 타입 통합 / 특성 숫자컬럼 추가

# ### 1-1-1. 데이터 타입 통합

# In[4]:


# featuresData.info()


# In[5]:


# 주의할 사항은 모든 컬럼에 대해서 고정시키는걸 고려햐는게 나을수도 있다
featuresData.QTY = featuresData.QTY.astype(float)


# ### 1-1-2. 특성 값 숫자컬럼 변경

# In[6]:


def valueClustering(inValue):
    if inValue == "Y":
        outValue = 1
    else:
         outValue = 0
    return outValue

featuresData["HOLIDAY_NEW"] = featuresData.HOLIDAY.apply(valueClustering)
featuresData["PROMOTION_ NEW"] = featuresData.PROMOTION.apply(valueClustering)

featuresData.head(3)


# LabelEncoder 사용법

# In[ ]:


# from sklearn.preprocessing import LabelEncoder
# # 머신러닝/딥러닝 Label인코더 -> 문자 -> 숫자로 매핑시켜준다.
# holiEn = LabelEncoder()
# # featuresData.HOLIDAY를 알아서 1, 0 으로 변환시켜준다.
# featuresData["HOLIDAY_LABEL_EN"] = holiEn.fit_transform(featuresData.HOLIDAY)
# # 다시 전 단계로 돌아간다.
# featuresData["HOLIDAY_DE"] = holiEn.inverse_transform(featuresData.HOLIDAY_LABEL_EN)
# # 결과값이 달라졌는지 확인하기 위함
# featuresData.loc[featuresData.HOLIDAY != featuresData.HOLIDAY_DE]


# ### 1-2. 특성 선정 / 데이터 분리

# ### 1-2-1. 특성 선정

# In[8]:


corrDf = featuresData.corr()
standardLimit = 0.5
features = list(corrDf.loc[ ( abs(corrDf.QTY) > standardLimit ) & (corrDf.QTY != 1) ].index )
label = ["QTY"]


# ### 1-2-2. 데이터 분리

# In[12]:


# features: 문제지 / label: 정답지

standardIndex = 0.8
# featuresData.shape
sortKey = ["REGIONID","ITEM","YEARWEEK"]
sortedData = featuresData.sort_values(sortKey, ignore_index=True)

# 정렬하고 80%에 있는 인덱스의 번호로 분리
# sortedData.shape
selectedIndex = int( list( sortedData.shape )[0] * standardIndex )

yearweekStd = sortedData.loc[selectedIndex].YEARWEEK


# In[ ]:


print(sortedData.shape)


# In[18]:


# 훈련데이터와 테스트데이터를 (문제지와 정답지로 구분해서 정의한다.)

# 훈련데이터
trainingDataFeatures = sortedData.loc[sortedData.YEARWEEK <= yearweekStd, features]
trainingDataLabel = sortedData.loc[sortedData.YEARWEEK <= yearweekStd, label]

# 테스트 데이터
testDataFeatures = sortedData.loc[sortedData.YEARWEEK > yearweekStd, features]
testDataLabel = sortedData.loc[sortedData.YEARWEEK > yearweekStd, label]


# In[ ]:


print(testDataLabel.shape)


# ### 2. 모델적용

# ### 2-1. 모델 적용

# ### 2-1-1 학습

# In[19]:


# 모델 선언 (Decision, Random)
model_dt = DecisionTreeRegressor(random_state=10, max_depth=1)
model_rf = RandomForestRegressor(random_state=10)
model_lr = LinearRegression()


# In[20]:


model_dt.fit(X=trainingDataFeatures, y=trainingDataLabel)
model_rf.fit(X=trainingDataFeatures, y=trainingDataLabel)
model_lr.fit(X=trainingDataFeatures, y=trainingDataLabel)


# ### 3. 예측

# In[21]:


predictValueDt = model_dt.predict(testDataFeatures)
predictValueRf = model_rf.predict(testDataFeatures)
predictValueLr = model_lr.predict(testDataFeatures)


# In[22]:


testDataAll = featuresData.loc[ testDataFeatures.index ] 


# In[23]:


testDataAll["PREDICT_DT"] = predictValueDt
testDataAll["PREDICT_RF"] = predictValueRf


# In[24]:


testDataAll["PREDICT_LR"] = predictValueLr


# In[ ]:


# 장점
# DecisionTree => 과거의 경험치를 그대로 반영, 변동성이 큰 데이터에서 강함 / 설명력이 강함
# 단점 
# 오버피팅 문제 [너무 과거에 매어있음]
# 해결 : randomforest 
# 장점 : DecisionTree의 오버피팅을 해결
# 단점 : 설명력이 조금 어렵다.
# 기타 : 
# AutoMl -> 모델을 기계가 알아서 선택


# In[25]:


predictDtMae = mean_absolute_error(y_true=testDataAll.QTY, y_pred=testDataAll.PREDICT_DT )
predictRfMae = mean_absolute_error(y_true=testDataAll.QTY, y_pred=testDataAll.PREDICT_RF )
predictLrMae = mean_absolute_error(y_true=testDataAll.QTY, y_pred=testDataAll.PREDICT_LR )


# In[26]:


errorReportDf = pd.DataFrame( [[ predictDtMae, predictRfMae,predictLrMae     ]],
            columns=["DT_MAE","RF_MAE","LR_MAE"])


# In[27]:


errorReportDf


# In[28]:


features


# In[29]:


# 대휴일 1 소휴일 4
userInputHCLUS = 1
# 제품 할인 %
userInputProPercent=0.5
# 홀리데이 유무 Y= 1 N = 0
userInputHoilidayYn = 1
# 프로모션 유무 Y=1 N= 0
userInputPromotionYn = 1


# In[30]:


futureData = pd.DataFrame([[ userInputHCLUS,
              userInputProPercent,
              userInputHoilidayYn,
              userInputPromotionYn]]   )


# In[31]:


# pickle 파일로 저장가능하다.
model_dt.predict(futureData)


# In[32]:


trainingDataFeatures.shape


# In[33]:


treeStep1 = trainingDataFeatures.loc[trainingDataFeatures.PRO_PERCENT > 0.259]


# In[34]:


treeStep2 = treeStep1.loc[treeStep1.PRO_PERCENT > 0.294]


# In[35]:


treeStep3 = treeStep2.loc[treeStep2.HCLUS > 0.5]


# In[36]:


treeStep3.index


# In[37]:


featuresData.loc[  treeStep3.index ]


# In[38]:


trainingDataLabel.loc[treeStep3.index].QTY.mean()


# # graphviz 시각화

# In[39]:


from sklearn.tree import export_graphviz
import graphviz

export_graphviz(decision_tree=model_rf.estimators_[30],
                out_file="tree.dot",
                impurity=True)
with open("tree.dot") as f:
    dot_graph = f.read()
display(graphviz.Source(dot_graph))


# # 모델 저장

# In[40]:


import pickle


# In[41]:


filename = 'finalized_model.sav'
pickle.dump(model_dt, open(filename, 'wb'))


# In[ ]:




