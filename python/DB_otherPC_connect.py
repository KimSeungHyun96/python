#!/usr/bin/env python
# coding: utf-8

# ##### 1. 상대경로/절대경로
# ##### 2. 데이터불러오기 (pandas ~ csv ~ sep > ("") 활용법 기억)
# ##### 3. 데이터 불러올 경우 한글 유의 encoding="ms949"
# ##### 4. to_csv 저장할 때 index가 생기기 때문에 index=False 사용
# ##### 5. data.columns = ["SALESID", "REGIONNAME"]
# ##### // data.rename( columns={"SALESID":"SID", "REGIONNAME":"SNAME"], inplace=True)
# ##### inplace=False는 따로 변수를 만들어 넣어줌 =True는 바로 적용됨

# In[ ]:


# 클립보드 사용시 엑셀에서 드래그시 클립보이에 들어감
pd.read_clipboard()


# ## csv 파일 읽기

# In[1]:


import pandas as pd

selloutData = pd.read_csv("../dataset/kopo_product_volume.csv")

selloutData.head()


# ## 내 PC의 csv파일을 데이터베이스에 저장

# In[1]:


import pandas as pd
import psycopg2
from sqlalchemy import create_engine

selloutData = pd.read_csv("../dataset/kopo_product_volume.csv")

selloutData.head()

selloutData.columns = ["regionid", "productgroup", "yearweek", "volume"]

selloutData.to_csv("../dataset/kopo_product_volume.csv")

engine = create_engine("postgresql://postgres:postgres@127.0.0.1:5432/postgres")

resultname = "kopo_product_volume"

selloutData.to_sql(name=resultname, con=engine, if_exists='replace', index=False)

indata = pd.read_sql_query("select * from kopo_product_volume", engine)

engine.dispose()

indata.head()


# ## 다른 PC에 테이블 넣기

# In[ ]:


import pandas as pd

targetData = "../dataset/kopo_product_volume.csv"

indata = pd.read_csv(targetData, encoding="ms949")

indata.columns = ["regionid_SH", "pg_SH", "yw_SH", "vl_SH"]

import psycopg2
from sqlalchemy import create_engine

# mylocalpgUrl = "postgresql://postgres:postgres@127.0.0.1:5432/postgres"

KimNamUrl = "postgresql://postgres:postgres@192.168.110.17:5432/postgres"

engine_pg = create_engine(KimNamUrl)

resultTableName = "pg_out_KSH"



indata.to_sql(name=resultTableName, con=engine_pg, 
           if_exists="replace", index=False)

#targetData = "pg_out"

# sqlReadData = pd.read.sql(sql="select * from pg_out", con=engine_pg, engine = engine_pg)
pd.read_sql_table(table_name="pg_out_KSH", con=engine_pg)


# ## 다른PC의 데이터를 내 PC로 가져오기 (+컬럼변경)

# In[14]:


# 다른 PC의 테이블 보기
# 다른 PC의 postgres의 아이디 비밀번호 아이피, 테이블를 알아야 함
import pandas as pd 
import psycopg2
from sqlalchemy import create_engine 

KimNamUrl = create_engine("postgresql://postgres:postgres@192.168.110.17:5432/postgres")

engine_pg = KimNamUrl

resultTableName = "kopo_product_volume"

data = pd.read_sql_table(table_name="kopo_product_volume", con=engine_pg)
# sqlReadData = pd.read.sql(sql="select * from pg_out", con=engine_pg, engine = engine_pg)
data


# In[15]:


# 다른 PC의 테이블을 내 PC로 저장
import pandas as pd 
import psycopg2
from sqlalchemy import create_engine 

mylocalpgUrl = create_engine("postgresql://postgres:postgres@127.0.0.1:5432/postgres") 

engine_pg = mylocalpgUrl

resultTableName = "kopo_product_volume_sh"

data.columns = ["regionid_sh", "pg_sh", "yw_sh", "vl_sh"]

data.to_sql(name=resultTableName, con=engine_pg, if_exists="replace", index=False)

data = pd.read_sql_table(table_name="kopo_product_volume_sh", con=engine_pg)
# sqlReadData = pd.read.sql(sql="select * from pg_out", con=engine_pg, engine = engine_pg)
data


# ## 다른 PC에 넣는 다른방법

# In[ ]:


targetDbIp = "192.168.110.111"
targetDbPort = "5432"
targetDbId = "kopo"
targetDbPw = "kopo"
targetDbName = "kopodb"
#111 5432 kopo kopo kopo

targetDbpreFix = "postgres://"

targetUrl = "{}{}:{}@{}:{}/{}".format(targetDbpreFix,targetDbId,targetDbPw,targetDbIp,targetDbPort,targetDbName)

pg_kopo_engine = create_engine(targetUrl)

tableName = "pgout_kopo_ksh"

indata.to_sql(name=tableName, con=pg_kopo_engine, if_exists="replace", index=False)

