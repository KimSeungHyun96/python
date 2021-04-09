#!/usr/bin/env python
# coding: utf-8

# In[3]:


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

try:
    indata.to_sql(name=tableName, con=pg_kopo_engine, if_exists="replace", index=False)
    print("{} unload 성공".format(tableName))
except Exception as e:
    print(e)


# In[ ]:




