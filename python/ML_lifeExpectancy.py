#!/usr/bin/env python
# coding: utf-8

# Author: 김승현 \
# Created: 2021.06.22 \
# Description: sklearn, graphviz, matplotlib 
#    > sklearn_model을 통해 (나라, 년도, 기대수명, 성인 사망률, 알코올)기준 상관관계 분석\
#    > 성인 사망률 : 성별의 성인 사망률(인구 1000명당 15~60년 사망 확률)\
#    > 알코올 1인당 소비량을 통해 성인 사망률, 기대수명을 비교 상관관계가 있음을 확인(DecisionTreeRegressor)

#    > 머신러닝 지도학습(회귀 : Linear Regression, Decision Tree, Random Forest) 사용 \
#    > 데이터를 전처리하여 특성을 선정하고 분리함 \
#    > 모델을 학습하고 예측하여 정확도를 측정(MAE, MSE, RMSE, MAPE) \
#    > graphviz : Tree(Decision Tree, Random Forest), matplotlib : Linear Regression 시각화

# Prerequisites : Install graphviz, sklearn, matplotlib

# ### 라이브러리 정의

# 데이터 처리 라이브러리
import pandas as pd
import numpy as np
# 분석알고리즘 DecisionTree 구현 라이브러리
from sklearn.tree import DecisionTreeRegressor # 설명도가 높아짐
from sklearn.ensemble import RandomForestRegressor  # 설명은 낮지만 정확도가 높아짐
from sklearn.linear_model import LinearRegression # YES or NO

# 분석 Regression 평가 대표 지표 (MAE, MSE)
from sklearn.metrics import mean_absolute_error # MAE
from sklearn.metrics import mean_squared_error # MSE

# plot 시각화
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import platform
# graphviz 시각화
from sklearn.tree import export_graphviz
import graphviz


# ### 데이터 불러오기
lifeData = pd.read_csv("./dataset/life_expectancy_data.csv")
# lifeData.head()


# ### 1. 데이터 전처리
# 
# ### 1-1. 데이터 정제 / 타입 통합특성

# ### 1-1-1. 데이터 정제

# 한국, 년도, 기대수명, 성인 사망률, 알코올 기준
lifeData = lifeData[["Country","Year","LifeExpectancy","AdultMortality","Alcohol"]]
lifeData = lifeData[lifeData.Country == "Democratic People's Republic of Korea"].reset_index(drop=True)
lifeData.dropna(inplace=True)


# ### 1-1-2. 데이터 타입 통합
# lifeData.info()

# 데이터 형변환
typeKey = ["Year","LifeExpectancy","AdultMortality","Alcohol"]
lifeData[typeKey]=lifeData[typeKey].astype(float)
# LifeData.dtypes

# lifeData.head()


# ### 1-2. 특성 선정 / 데이터 분리
# 
# ### 1-2-1. 특성 선정

LABELCOLUMN = "LifeExpectancy"

# 상관관계 계수 측정
corrDf = lifeData.corr()

standardLimit = 0.5
features = list(corrDf.loc[ ( abs(corrDf.LifeExpectancy) > standardLimit ) & (corrDf.LifeExpectancy != 1) ].index )
features

label = [LABELCOLUMN]

# #### 1-2-2. 데이터 분리

# 8 : 2 로 나누기 위함(문제지, 정답지)
standardIndex = 0.8
# featuresData.shape
sortKey = ["Year","AdultMortality","Alcohol"]
sortedData = lifeData.sort_values(sortKey, ignore_index=True)

# 정렬하고 80%에 있는 인덱스의 번호로 분리
selectedIndex = int( list( sortedData.shape )[0] * standardIndex )

yearStd = sortedData.loc[selectedIndex].Year

print(sortedData.shape)

# 훈련용 데이터
trainingDataFeatures = sortedData.loc[sortedData.Year <= yearStd, features]
trainingDataLabel = sortedData.loc[sortedData.Year <= yearStd, label]

# 테스트 데이터
testDataFeatures = sortedData.loc[sortedData.Year > yearStd, features]
testDataLabel = sortedData.loc[sortedData.Year > yearStd, label]

print(trainingDataFeatures.shape)
print(trainingDataLabel.shape)
print(testDataFeatures.shape)
print(testDataLabel.shape)

# ### 2. 모델적용
# 
# ### 2-1. 모델 적용
# 
# ### 2-1-1 학습 (DecisionTree, RandomForest, Linear)

# 모델 선언 (Decision, Random) / 하이퍼 파라미터 튜닝
model_dt = DecisionTreeRegressor(random_state=10, max_depth=1)
model_rf = RandomForestRegressor(random_state=10)
model_lr = LinearRegression()

model_dt.fit(X=trainingDataFeatures, y=trainingDataLabel)
model_rf.fit(X=trainingDataFeatures, y=trainingDataLabel)
model_lr.fit(X=trainingDataFeatures, y=trainingDataLabel)


# ### 3. 예측 (DecisionTree, RandomForest, Linear)
predictValueDt = model_dt.predict(testDataFeatures)
predictValueRf = model_rf.predict(testDataFeatures)
predictValueLr = model_lr.predict(testDataFeatures)

testDataAll = lifeData.loc[ testDataFeatures.index ] 

# ### 4. 데이터 정리

testDataAll["PREDICT_DT"] = predictValueDt
testDataAll["PREDICT_RF"] = predictValueRf
testDataAll["PREDICT_LR"] = predictValueLr


# ### 5. 정확도 측정 (MAE, MSE, RMSE, MAPE) / 결과 검증 단계
trueLifeData = testDataAll.LifeExpectancy

# MAE (Mean Absolute Error)
# mae는 실제 값과 예측 값의 차이(Error)를 절대값으로 변환해 평균화(차이들의 평균값) / 이상치 많을때
predictDtMae = mean_absolute_error(y_true=trueLifeData, y_pred=testDataAll.PREDICT_DT )
predictRfMae = mean_absolute_error(y_true=trueLifeData, y_pred=testDataAll.PREDICT_RF )
predictLrMae = mean_absolute_error(y_true=trueLifeData, y_pred=testDataAll.PREDICT_LR )

# MSE (Mean Squared Error)
# mse 실제 값과 예측 값의 차이를 제곱해 평균화 / 특이값이 존재하면 수치가 상승
predictDtMse = mean_squared_error(y_true=trueLifeData, y_pred=testDataAll.PREDICT_DT )
predictRfMse = mean_squared_error(y_true=trueLifeData, y_pred=testDataAll.PREDICT_RF )
predictLrMse = mean_squared_error(y_true=trueLifeData, y_pred=testDataAll.PREDICT_LR )

# RMSE (Root Mean Squared Error)
# rmse mse에 루트를 씌운 rmse 값을 사용 /에러에 제곱하기 때문에 
# 에러가 클 수록 그에 따른 가중치가 높이 반영, 에러에 따른 손실이 올라가는 상황에서 사용
predictDtRmse = np.sqrt( mean_squared_error(y_true=trueLifeData, y_pred=testDataAll.PREDICT_DT))
predictRfRmse = np.sqrt( mean_squared_error(y_true=trueLifeData, y_pred=testDataAll.PREDICT_RF))
predictLrRmse = np.sqrt( mean_squared_error(y_true=trueLifeData, y_pred=testDataAll.PREDICT_LR))

# MAPE (Mean Absolute Percentage Error)
# mape mae를 퍼센트로 변환 mae와 같은 단점 / 모델에 대한 평향이 존재
testDataAll["DT_MAPE"]=1 - abs(trueLifeData-testDataAll.PREDICT_DT) / trueLifeData
testDataAll.loc[trueLifeData < 0, "DT_MAPE"] = 0

testDataAll["RF_MAPE"]=1 - abs(trueLifeData-testDataAll.PREDICT_RF) / trueLifeData
testDataAll.loc[trueLifeData < 0, "RF_MAPE"] = 0

testDataAll["LR_MAPE"]=1 - abs(trueLifeData-testDataAll.PREDICT_LR) / trueLifeData
testDataAll.loc[trueLifeData < 0, "LR_MAPE"] = 0

# ### 6. Error Report

# MAE ErrorReport (DecisionTree, RandomForest, Linear)
maeErrorReport = pd.DataFrame([[predictDtMae, predictRfMae,predictLrMae]],
            columns=["DT_MAE","RF_MAE","LR_MAE"])
maeErrorReport

# MSE ErrorReport (DecisionTree, RandomForest, Linear)
mseErrorReport = pd.DataFrame([[predictDtMse, predictRfMse,predictLrMse]],
            columns=["DT_MSE","RF_MSE","LR_MSE"])
mseErrorReport

# RMSE ErrorReport (DecisionTree, RandomForest, Linear)
rmseErrorReport = pd.DataFrame([[predictDtRmse, predictRfRmse,predictLrRmse]],
            columns=["DT_RMSE","RF_RMSE","LR_RMSE"])
rmseErrorReport

# MAPE ErrorReport (DecisionTree, RandomForest, Linear)
mapeErrorReport = testDataAll[["DT_MAPE","RF_MAPE","LR_MAPE"]]
mapeErrorReport


# ### 7. graphviz 시각화

# DecisionTree 시각화
export_graphviz(decision_tree=model_dt,
                out_file="tree.dot",
                impurity=True,
                rounded=True,
                filled=True)
with open("tree.dot") as f:
    dot_graph = f.read()
display(graphviz.Source(dot_graph))

# RandomForest 시각화
export_graphviz(decision_tree=model_rf.estimators_[30],
                out_file="tree.dot",
                impurity=True,
                rounded=True,
                filled=True)
with open("tree.dot") as f:
    dot_graph = f.read()
display(graphviz.Source(dot_graph))

try:
    if platform.system() == 'Windows':
        #윈도우인 경우
        font_name = font_manager.FontProperties(fname="c:/Windows/fonts/malgun.ttf").get_name()
        rc('font', family=font_name)
    else:
        #Mac인 경우
        rc('font', family='AppleGothic')
except:
    pass
# 팝업 창 활용하여 차트 시연
LifeExpectancyData = lifeData[1:]
x=LifeExpectancyData.Year
y=LifeExpectancyData.AdultMortality
y2=LifeExpectancyData.Alcohol
y3=LifeExpectancyData.LifeExpectancy

# 이중축
fig = plt.figure(figsize=(14,5))
ax1 = fig.add_subplot(1,2,1)
#figure, ax1 = plt.subplots(figsize=(10,5))
ax1.plot(x,y, 'bo-',lw=1.5, label = '성인 사망률')
ax1.grid(True)
ax1.legend(loc=9)
ax1.set_ylabel('AdultMortality')
ax1.set_xlabel('Year')
plt.title('알코올 대비 성인 사망률')
ax2 = ax1.twinx()
ax2.plot(x,y2, 'go-', lw=1.5, label='알코올')
ax2.legend(loc=8)
ax2.set_ylabel('Alcohol')
# 두번째 차트
ax3 = fig.add_subplot(1,2,2) 
ax3.plot(x,y3, 'b-', lw=1.5, label='기대 수명') 
ax3.grid(True) 
ax3.legend()
ax3.set_xlabel('Year')
ax3.set_ylabel('LifeExpectancy')
ax3.set_title('기대 수명 (Republic of Korea)')


# ### 8. 모델 저장
import pickle

filename = 'finalLife_model.sav'
pickle.dump(model_dt, open(filename, 'wb'))
pickle.dump(model_rf, open(filename, 'wb'))
pickle.dump(model_lr, open(filename, 'wb'))

