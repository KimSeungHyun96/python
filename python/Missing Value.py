#!/usr/bin/env python
# coding: utf-8

# # Python 결측 값 다루기

# In[5]:


# PANDAS 패키지 불러오기
import pandas as pd
import numpy as np


# In[6]:


sampleData = pd.read_excel("../dataset//missingValue.xlsx")
sampleData.head()


# In[ ]:


filtered_df = df[df['name'].notnull()]


# In[9]:


sampleData[   sampleData['product'].notnull() ]


# In[4]:


sampleData[   sampleData.qty.notnull()]


# ###  컬럼별 결측값 개수확인하기

# In[3]:


sampleData.isnull().sum()


# In[4]:


sampleData['qty'].isnull().sum()


# In[5]:


sampleData.notnull().sum()


# ### 결측값 채우기

# #### 1. 특정 값으로 채우기

# In[7]:


aa = sampleData.fillna("")


# In[8]:


aa


# In[8]:


sampleData


# #### 2. 특정 순서로 채우기

# In[9]:


sampleData


# ### 백필 뒷부분 채우기

# In[10]:


sampleData.fillna(method="bfill")


# In[11]:


sampleData


# In[12]:


sampleData.fillna(method="ffill")


# #### 3. 평균 값으로 채우기

# In[13]:


sampleData


# In[14]:


sampleData.fillna(sampleData.mean())


# In[15]:


sampleData


# In[16]:


sampleData.where(pd.notnull(sampleData), sampleData.mean(), axis='columns')


# In[17]:


sampleData.fillna(sampleData.mean()['qty':'target'])


# #### 4. 다른 컬럼의 값으로 채우기

# In[18]:


sampleData['new_qty'] = np.where(pd.notnull(sampleData['qty']) == True, 
                                 sampleData['qty'], sampleData['target'])
sampleData['new_target'] = np.where(pd.notnull(sampleData['target']) == True, sampleData['target'], 
                                    sampleData['qty'])
sampleData


# In[19]:


sampleData

