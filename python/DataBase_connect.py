#!/usr/bin/env python
# coding: utf-8

# ##### 1. 상대경로/절대경로
# ##### 2. 데이터불러오기 (pandas ~ csv ~ sep > ("") 활용법 기억)
# ##### 3. 데이터 불러올 경우 한글 유의 encoding="ms949"
# ##### 4. to_csv 저장할 때 index가 생기기 때문에 index=False 사용
# ##### 5. data.columns = ["SALESID", "REGIONNAME"]
# ##### // data.rename( columns={"SALESID":"SID", "REGIONNAME":"SNAME"], inplace=True)
# ##### inplace=False는 따로 변수를 만들어 넣어줌 =True는 바로 적용됨

# In[4]:


import pandas as pd


# In[4]:


carDataUrlPath = "https://raw.githubusercontent.com/hyokwan/python-lecture/master/dataset/cars.csv"


# In[31]:


data = pd.read_csv("../dataset/kopo_region_mst_hangul.csv", encoding="ms949")


# In[32]:


data.columns = ["SALESID", "REGIONNAME"]


# In[41]:


data.rename( columns={"SALESID":"SID", "REGIONNAME":"SNAME"}, inplace=True )


# ## --

# In[1]:


import pandas as pd


# In[8]:


targetData = "../dataset/kopo_product_volume.csv"


# In[9]:


data = pd.read_csv(targetData, encoding="ms949").head()


# In[10]:


data.columns = ["regionid", "productgroup", "yearweek", "volume"]


# # --

# In[5]:


import pandas as pd
import psycopg2
from sqlalchemy import create_engine

indata = pd.read_csv("../dataset/kopo_decision_tree_all_new.csv")

indata.shape

# .columns = 컬럼보기 / .str추가 = 문자열 / .lower() 컬럼 소문자로 변환
indata.columns.str.lower()

targetDbIp = "192.168.110.111"
targetDbPort = "5432"
targetDbId = "kopo"
targetDbPw = "kopo"
targetDbName = "kopodb"

targetDbpreFix = "postgres://"

targetUrl = "{}{}:{}@{}:{}/{}".format(targetDbpreFix,targetDbId,targetDbPw,targetDbIp,targetDbPort,targetDbName)

pg_kopo_engine = create_engine(targetUrl)

tableName = "pgout_kopo_sh"

indata.to_sql(name=tableName, con=pg_kopo_engine, if_exists="replace", index=False)


# In[ ]:


# pandas, psycopg2 postgres를 연결시키기 위해 사용
import psycopg2
import pandas as pd
from sqlalchemy import create_engine 
# d6tstack = 성능향상
import d6tstack

# DB 커넥션 열기
purl = 'postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/postgres' 
engine = create_engine(purl) 
# DB 테이블을 읽어 Data Frame 변수에 저장하기
selloutData = pd.read_sql_query('SELECT * FROM kopo_product_volume', engine) 
selloutData.head()
# 컬럼해더 재정의
selloutData.columns = ['regionid','pg','yearweek','volume']
# 데이터 저장
resultname='pgresult'
d6tstack.utils.pd_to_psql(df=selloutData, uri=purl, table_name=resultname, if_exists='replace')

