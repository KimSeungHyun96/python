#!/usr/bin/env python
# coding: utf-8

# ### For, While 반복문

# In[1]:


targetList = ["UN001", "UN002", "UN003", "UN004"]


# In[2]:


preFix = "LEDTV_"


# In[5]:


targetList[0] = preFix + targetList[0]
targetList[1] = preFix + targetList[1]
targetList[2] = preFix + targetList[2]
targetList[3] = preFix + targetList[3]


# In[ ]:


targetListlen = len(targetList)


# In[5]:


# i를 0부터 4까지 1씩 증가
# for문의 헤더가 끝나는 지점 ":"을 써줘야 한다.
# 구문은 tab 들여쓰기로 컴퓨터가 인식하게 해준다.
for i in range(0, 4, 1): # for문 헤더
# for i in range(0, targetListlen, 1):
    targetList[i] = preFix + targetList[i]


# In[3]:


i=0
# while문의 헤더의 종결점은 ":" 써줘야한다.
# 구문은 tab 들여쓰기를 해야한다.
while (i < 4):
    targetList[i] = preFix + targetList[i]
    # while 문은 반복문 마지막에 자동증가 안해줌!
    i=i+1


# In[4]:


targetList


# #### tvList2 = [ 'UN40EN001', 'UN40EN002’, 'UN40EN003', 'UN40EN004’] 리스트가 출력되도록 하세요

# In[2]:


tvList2 = [ 'UN40EN001', 'UN40EN002', 'UN40EN003', 'UN40EN004']

tvList2Len = len(tvList2)

for i in range(0, tvList2Len):
    tvList2[i] = tvList2[i]

tvList2


# In[3]:


tvList2 = [ 'EN001', 'EN002', 'EN003', 'EN004']

preFix = 'UN40'

tvList2Len = len(tvList2)

for i in range(0, tvList2Len):
    tvList2[i] = preFix + tvList2[i]

tvList2


# In[4]:


scoreList = [50, 60, 70, 100]


# In[5]:


scoreLabel = "D"


# In[12]:


score = 80


# In[13]:


if score < 50:
    scoreLabel = "E"
elif score < 60:
    scoreLabel = "D"
elif score < 70:
    scoreLabel = "C"
else:
    scoreLabel = "B"


# In[14]:


scoreLabel


# In[ ]:


# Step1: 리스트에 있는 데이터를 하나씩 확인하자
# Step2: 리스트 아이템 별 preFix 개수를 확인하자
# Step3: preFix >= 2 "LEDTV_LEDTV_UN"
#        preFix == 1 -> pass
#        preFix < 1  -> preFix를 붙이자


# #### tvList2 = [ 'UN40EN001', 'LEDTV_UN40EN002', 'LEDTV_LEDTV_UN40EN003’, ‘UN40EN004’]리스트에서 LEDTV_가 한 개만 앞에 붙도록 하세요 (대소문자 구분없이 전부 처리)
# 

# In[6]:


tvList2 = [ 'UN40EN001', 'LEDTV_UN40EN002', 'LEDTV_LEDTV_UN40EN003', 'UN40EN004']

preFix = 'LEDTV_'

tvList2Len = len(tvList2)

for i in range(0, tvList2Len):
    tvList2Count = tvList2[i].count(preFix)
    tvList2Count
    if (tvList2Count == 0):
        tvList2[i] = preFix + tvList2[i]
    elif (tvList2Count >= 1):
        tvList2[i] = tvList2[i].replace(preFix, "")
        tvList2[i] = preFix + tvList2[i]
    else:
        tvList2[i] = preFix + tvList2[i]

tvList2


# #### nationList [‘A01’ , ‘한국’ , ‘A02’ , ‘미국’ , ‘A03’ , ‘프랑스’] 국가코드만 출력하세요

# In[ ]:





# ### tvList2 = [ 'UN40EN001', 'LEDTV_UN40EN002', 'LEDTV_LEDTV_UN40EN003’, ‘ledtv_UN40EN004’] 리스트에서 LEDTV_가 한 개만 앞에 붙도록 하세요 (* 대소문자 구분없이 전부 처리!)

# #### While 사용

# In[2]:


tvList2 = [ 'UN40EN001', 'LEDTV_UN40EN002', 'LEDTV_LEDTV_UN40EN003', 'ledtv_UN40EN004']

preFix = 'LEDTV_'

tvList2Len = len(tvList2)

i=0
while (i < tvList2Len):
    tvList2[i] = tvList2[i].upper()

    if (tvList2[i] == 0):
        tvList2[i] = preFix + tvList2[i]
    elif (tvList2[i] == 1):
        tvList2[i] = tvList2[i]
    else:
        tvList2[i] = tvList2[i].replace(preFix, "")
        tvList2[i] = preFix + tvList2[i]
    i=i+1

tvList2


# #### For 사용

# In[3]:


tvList2 = [ 'UN40EN001', 'LEDTV_UN40EN002', 'LEDTV_LEDTV_UN40EN003', 'ledtv_UN40EN004']

preFix = 'LEDTV_'

tvList2Len = len(tvList2)

for i in range(0, tvList2Len):
    tvList2upp = tvList2[i].upper()

    if tvList2upp.count(preFix) >= 2:
        tvList2[i] = tvList2[i].replace(preFix, "")
        tvList2[i] = preFix + tvList2[i]
    elif tvList2upp.count(preFix) == 1:
        tvList2[i] = tvList2upp
    else:
        tvList2[i] = preFix + tvList2[i]

tvList2


# #### For 사용(2)

# In[1]:


tvList2 = [ 'UN40EN001', 'LEDTV_UN40EN002', 'LEDTV_LEDTV_UN40EN003', 'ledtv_UN40EN004']

preFix = 'LEDTV_'

tvList2Len = len(tvList2)

for i in range(0, tvList2Len):
    tvList2[i] = tvList2[i].upper()

    if (tvList2[i] == 0):
        tvList2[i] = preFix + tvList2[i]
    elif (tvList2[i] == 1):
        tvList2[i] = tvList2[i]
    else:
        tvList2[i] = tvList2[i].replace(preFix, "")
        tvList2[i] = preFix + tvList2[i]

tvList2


# ##### SCORE  변수를 80으로 선언 후90점이상 A, 80~90점 B, 이외 C 점수로
# GRADE변수에 할당하는 프로그램을 구현하세요
# 

# In[24]:


score = 80

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"

grade


# ## 반복 프로세스 함수화

# In[4]:


a = 10
b = 5.3


# In[5]:


revenue = a/b


# In[6]:


revenue


# In[7]:


round(revenue, 2)


# ### 미션 소수점 둘째 자리 반올림

# In[1]:


def roundFunction(inValue):
    # Step1: 입력받은 데이터를 반올림 자리수만큼 곱해준다.
    # 함수를 개발하기 위한 디버깅 코드
    # inValue = 1.8934309034900002
    step1 = inValue * 100

    # Step2: 곱해준 결과에 0.5를 더한 후 소수점이하 버림
    step2 = int(step1 + 0.5)

    # Step3: 100으로 나누어준다.
    step3 = step2 / 100
    outValue = step3

    return outValue


# In[2]:


roundFunction(1.34567890)


# In[2]:


displatedRevenue = roundFunction(revenue)

displatedRevenue


# In[12]:


accuracy = 89.1232423


# In[13]:


displatedaccuracy = roundFunction(accuracy)
displatedaccuracy


# #### 지역변수 / 전역변수 이해

# In[24]:


globalVar = 0.5


# In[25]:


def roundFunction(inValue1, inValue2):
    inValue1 = 0.5
    inValue2 = 0.3
    meanValue = 1.0
    # 분모가 0인 경우 기본값 1
    if inValue2 != 0:
        meanValue = inValue1 / inValue2
    else:
        outValue = meanValue

    return outValue


# In[27]:


print(globalVar)
print(meanValue) # 지역변수는 출력 X


# #### 함수 입력변수에 따라 소수점 2자리수, 3자리 등의 반올림이 가능하도록 함수를 구현하세요 (예: roundFunction(12.2225,3) -> 3번째자리 반올림)

# ### 1.

# In[26]:


def roundFunction(inValue, option):
#   디버깅 코드
#   inValue = 12.2225
    step1 = inValue * (10**option)
    step2 = int(step1 + 0.5)
    step3 = step2 / (10**option)
    outVlaue = step3
    return outVlaue


# ### 2.

# In[14]:


inputValue = 12.2225


# In[15]:


def roundFunction(inValue, option):
    step1 = inValue * (10**option)
    inValue = int(step1 + 0.5)
    inValue = inValue / (10**option)
    outVlaue = inValue
    return outVlaue


# In[16]:


roundFunction(inputValue, 3)


# #### 추가 제어로직

# In[ ]:


# break (종료)

model = ["MODEL01","MODEL02"]
attatedModel = []
for i in range(0, len(model) ):
    if( model[i] == "MODEL01" ):
        break
    attatedModel.append(model[i])

print( model[i] )
print (attatedModel)


# In[ ]:


# continue (위로)

model = ["MODEL01","MODEL02"]
attatedModel = []

for i in range(0, len(model) ):
    if( model[i] == "MODEL01" ):
        continue
attatedModel.append(model[i])

print( model[i] )
print (attatedModel)


# In[ ]:


# pass (아래로)

model = ["MODEL01","MODEL02"]
attatedModel = []
for i in range(0, len(model) ):
    if( model[i] == "MODEL01" ):
        pass
attatedModel.append(model[i])

print( model[i] )
print (attatedModel)


# ### productList를 활용하여 모바일 스피커 에서 "003" 모델을 제외하고 출력하세요

# In[1]:


tvList = ["LEDTV_UN40EN001", "LEDTV_UN40EN002", "LEDTV_UN40EN003"]
mobileList = ["G3_MO001", "G3_MO002","G3_MO003"]
speakerList = ["BL_SP001", "BL_SP002", "BL_SP003"]

productList = [tvList, mobileList, speakerList]

for i in range (0, len(productList)):
    productlength = len(productList[i])
    for j in range (0, productlength):
        if (productList[i][j].split("_")[0] == "G3") &           (productList[i][j].split("_")[1] == "MO003"):
            break    
        if (productList[i][j].split("_")[0] == "BL") &           (productList[i][j].split("_")[1] == "SP003"):
            break
        print(productList[i][j])


# ### 예외처리

# In[1]:


import pandas as pd


# In[2]:


mergedSet = []


# In[3]:


for i in range(1, 4):
    try:
        fileName = "./a"+str(i)+".txt"
        mergedSet.append( pd.read_csv("./a"+str(i)+".txt") ) #예외가 발생 가능한 코드
    except Exception as e:
        print("에러파일명 : {}".format(fileName))
        print(e)


# In[4]:


mergedSet[1]


# In[5]:


mergedSet.append( pd.read_csv("./a1.txt") )
mergedSet.append( pd.read_csv("./a2.txt") )
mergedSet.append( pd.read_csv("./a3.txt") )


# In[6]:


mergedSet[2]


# ### 문자열로 구성된 리스트의 합계를 구하는 함수를 생성하세요

# In[2]:


inputList = ["1234","1234","22","11",11]

i=0
sum=0
while(i < len(inputList)):
    itemType = type(inputList[i])
    sum = sum + float(inputList[i])
    i=i+1
    

sum


# In[1]:


List = ["11", "22", "33"]

sum = 0

for i in range(0, len(List)):
    sum = sum + int(List[i])

sum


# In[ ]:





# In[ ]:





# In[ ]:




