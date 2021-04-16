#!/usr/bin/env python
# coding: utf-8

# ### 튜플

# In[2]:


# 수정가능

PriceList = [100,200,150,170]

PriceList[0] = 190


# In[11]:


PriceList


# In[7]:


# 수정 불가능

PriceTuple = {100,200,150,170}

PriceTuple[0] = 190


# In[10]:


PriceTuple


# In[8]:


PriceSet = set(PriceList)


# In[ ]:


PriceTuple1 = {100,200,150,170}


# In[ ]:


PriceSet1 = {100,150,200,170}
PriceSet2 = {100,139,210,170}
PriceSet3 = {100,139,200,150}


# In[ ]:


PriceSet1.intersection # (교집합)
PriceSet2.union # (합집합)
PriceSet3.difference # (차집합)


# In[ ]:


allWeek = {1,2,3,4,5,6}


# In[ ]:


existWeek = {1,2,3,5,6}


# ### 딕셔너리 key, value 형태로 저장을 한다.

# In[1]:


PriceSet = [10,20,30,40]
PriceSet = {"price", 20, 30, 40}


# In[ ]:


priceList = [10,20,30,40]


# In[2]:


yearweekList = [202021,202002,202003,202004]

valueDict["regionid] = ["A01", "A01", "A01","A01"]
# In[4]:


priceDict {"price": priceList,
           "yearweek": yearweekList}

priceDict["price"]

import pandas as pd

pd.DataFatme(priceDict)


# ###### dic = {"name":"sec","id":"300000","address":"suwon"}에서 “id”:”300000” 삭제하여 출력하세요{'name': 'sec', 'address': 'suwon’}

# In[11]:


dic = {"name":"sec","id":"300000","address":"suwon"}

dic.keys() # {'name': 'sec', 'id': '300000', 'address': 'suwon'} 

dic.pop("id") # "id" 요소 삭제

dic # 출력 {'name': 'sec', 'address': 'suwon'}


# In[13]:


import pandas as pd


# In[21]:


indata = pd.read_csv("../dataset/customerdata.csv")


# In[22]:


indata.head()


# In[ ]:


indata.rename(columns=("CUSTID:CUSTID11")) # 키를 잡고 바꿈


# ### 데이터프레임 list

# In[15]:


import pandas as pd


# In[16]:


productIdList = ["LEDTV", "LEDTV", "LEDTV", "LEDTV"]
yearweekList = [202121,202102,202103,202104]
volValueList = [100, 120, 130, 140]


# In[ ]:


# 테이블로 저장됨


# In[9]:


pd.DataFrame(productId, columns=["product"])


# ### 데이터프레임 list 

# ##### list에서 데이터프레임 만들기

# In[1]:


import pandas as pd

productIdList = ["LEDTV", "LEDTV", "LEDTV", "LEDTV"]
yearweekList = [202121,202102,202103,202104]
volValueList = [100, 120, 130, 140]

columnName = ["PRODUCT", "YEARWEEK", "VOLUME"]

pd.DataFrame( zip(productIdList,
                yearweekList,
                 volValueList), columns=columnName)


# In[14]:


import pandas as pd


# In[15]:


KSH = pd.DataFrame([
      ["A01", "202001", 100],
      ["A01", "202002", 12],
      ["A01", "202003", 130]])


# In[16]:


KSH.rename(columns={0:"regionid",
                    1:"yearweek",
                    2:"sales"})


# In[14]:


import numpy as np


# In[5]:


np.linspace(start=1, stop=100, num=20)


# In[3]:


import numpy as np


# In[25]:


np.random.randint(low=0, high=10, size=10)
np.random.randint(1,20,3)
np.random.randint(11)


# In[4]:


r = np.random.random(size=10)
for i in range(0, len(r)):
    r[i] = int(r[i]*10)


# In[5]:


r


# In[30]:


np.random.rand(3,2,3)


# ### 자신만의 데이터프레임 만들기

# In[1]:


import pandas as pd


# In[2]:


KSH = pd.DataFrame([
      [1, "김승현", 25],
      [2, "김승현1", 26],
      [3, "김승현2", 27]])


# In[3]:


KSH.rename(columns={0:"NO",
                    1:"NAME",
                    2:"AGE"})


# In[6]:


KSH


# In[21]:


import pandas as pd


# In[22]:


noList = [1, 2, 3]
nameList = ["김승현", "김승현1", "김승현2"]
ageList = [25, 26, 27]


# In[23]:


columnName = ["NO", "NAME", "AGE"]


# In[24]:


my = pd.DataFrame( zip(noList, nameList, ageList), columns=columnName )


# In[25]:


my


# In[8]:


columns = ["no", "name", "age"]


# In[9]:


my

