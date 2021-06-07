#!/usr/bin/env python
# coding: utf-8

# # 1. 데이터 시각화하기

# ### 1. 1차원 차트 그리기

# In[1]:


#필요 라이브러리 정의
import matplotlib.pyplot as plt

# 커맨드뷰에서 차트 시연
get_ipython().run_line_magic('matplotlib', 'inline')

x=[1,2,3,4,5,6,7,8,9,10]
y=[1,4,9,16,25,36,49,64,81,100]
plt.plot(x,y)


# In[2]:


#필요 라이브러리 정의
import numpy as np
import matplotlib.pyplot as plt

# 커맨드뷰에서 차트 시연
get_ipython().run_line_magic('matplotlib', 'inline')
# 팝업 창 활용하여 차트 시연

# 
x=list(range(1,11,1))
y=[]
for i in x:
    y.append(i**2)
#y = [i**2 for i in x]
plt.plot(x,y)


# ### 2. 차트 꾸미기 선색 및 크기 설정

# In[11]:


xList=list(range(1,11,1))


# In[12]:


xList


# In[13]:


y=[]


# In[15]:


for i in x:
    y.append(i**2)


# In[16]:


y


# In[3]:


#필요 라이브러리 정의
import matplotlib.pyplot as plt

# 커맨드뷰에서 차트 시연
get_ipython().run_line_magic('matplotlib', 'inline')
# 팝업 창 활용하여 차트 시연
x=list(range(1,11,1))
y=[]
for i in x:
    y.append(i**2)

# 차트 꾸미기
plt.plot(x,y, 'g', lw=4.5) #차트 선색 및 크기설정


# ### 3. 차트 꾸미기 (실습: 선 종류 변경)

# In[23]:


#필요 라이브러리 정의
import matplotlib.pyplot as plt

# 커맨드뷰에서 차트 시연
get_ipython().run_line_magic('matplotlib', 'inline')
# 팝업 창 활용하여 차트 시연
x=list(range(1,11,1))
y=[]
for i in x:
    y.append(i**2)

# 차트 꾸미기
plt.plot(x,y, "go-" ) #차트 내 '*' 표기


# ### 4. 차트 꾸미기 (실습: 라벨과 제목)

# In[1]:


import matplotlib.pyplot as plt

import matplotlib

font_name = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
matplotlib.rc('font', family=font_name)
print(font_name)


# In[2]:


#필요 라이브러리 정의
import matplotlib.pyplot as plt

# 커맨드뷰에서 차트 시연
get_ipython().run_line_magic('matplotlib', 'inline')
# 팝업 창 활용하여 차트 시연
x=list(range(1,11,1))
y=[]
for i in x:
    y.append(i**2)

plt.plot(x,y,"go--")
# 차트 꾸미기
plt.xlabel('index') # x축 라벨
plt.ylabel('value') # y축 라벨
plt.title('Simple plot_안녕') # 차트 제목


# In[8]:


#필요 라이브러리 정의
import matplotlib.pyplot as plt

# 커맨드뷰에서 차트 시연
get_ipython().run_line_magic('matplotlib', 'inline')
# 팝업 창 활용하여 차트 시연
x=list(range(1,11,1))
y=[]
for i in x:
    y.append(i**2)

plt.plot(x,y,"go--")
# 차트 꾸미기
plt.yticks(fontsize=10)
plt.xticks(fontsize=10)
## x,y축 라벨 크기 조정
plt.xlabel('index', fontsize=10) # x축 라벨
plt.ylabel('value', fontsize=10) # y축 라벨
## 차트 타이틀 크기조정
plt.title('Simple plot', fontsize=10) # 차트 제목


# ### 5. 차트 꾸미기 (실습: 특정구간 확대)

# In[4]:


#필요 라이브러리 정의
import matplotlib.pyplot as plt

# 커맨드뷰에서 차트 시연
get_ipython().run_line_magic('matplotlib', 'inline')
# 팝업 창 활용하여 차트 시연
x=list(range(1,11,1))
y=[]
for i in x:
    y.append(i**2)

plt.plot(x,y,"bo--")

# 차트 꾸미기
# 특정구간 확대
plt.xlim(3,7)
plt.ylim(10,40)


# ### 6. 차트 꾸미기 (실습: 레전드 설정)

# In[5]:


#필요 라이브러리 정의
import matplotlib.pyplot as plt

# 커맨드뷰에서 차트 시연
get_ipython().run_line_magic('matplotlib', 'inline')
# 팝업 창 활용하여 차트 시연
x=list(range(1,11,1))
y = [i**2 for i in x]
y2 = [i**2.2 for i in x]

# 차트 꾸미기, legend
plt.plot(x,y,"go--", label="first")
plt.plot(x,y2,"bo--", label="second")
plt.legend(loc=0)


# ### 7. 차트 꾸미기 (실습: 어노테이션)

# In[27]:


#필요 라이브러리 정의
import matplotlib.pyplot as plt

# 커맨드뷰에서 차트 시연
get_ipython().run_line_magic('matplotlib', 'inline')
# 팝업 창 활용하여 차트 시연
x=list(range(1,11,1))
y = [i**2 for i in x]
y2 = [i**2.2 for i in x]

# 차트 꾸미기, legend
plt.plot(x,y,"go--", label="first")
plt.plot(x,y2,"bo--", label="second")
plt.legend(loc=0)

# 화살표 시작지점
plt.annotate('point',xy=(2,3), xytext=(4,4),arrowprops=dict(color="blue", width=2))


# ### 8. 1차원 차트 꾸미기 (종합)

# In[12]:


#필요 라이브러리 정의
import matplotlib.pyplot as plt

# 커맨드뷰에서 차트 시연
get_ipython().run_line_magic('matplotlib', 'inline')
# 팝업 창 활용하여 차트 시연
x=list(range(1,11,1))
y=[]
for i in x:
    y.append(i**2)
plt.plot(x,y)

# 차트 꾸미기
plt.plot(x,y, 'b', lw=1.5) #차트 선색 및 크기설정
plt.plot(x,y, 'bo', ) #차트 내 'o' 표기
plt.grid(True) #그리드 표기
plt.xlabel('index') # x축 라벨
plt.ylabel('value') # y축 라벨
plt.title('Simple plot') # 차트 제목


# ### 실습

# featuresData를 활용하여 
# 2015년도 자료만 활용하여
# x축: week, y축: qty를 라인차트로 그리세요

# In[13]:


import pandas as pd
featuresData =  pd.read_csv("../dataset/feature_regression_example.csv")


# In[14]:


import pandas as pd

featuresData =  pd.read_csv("../dataset/feature_regression_example.csv")

featuresData2015 = featuresData[ (featuresData.YEARWEEK >= 201501) &
                                (featuresData.YEARWEEK <= 201552)]

featuresData2016 = featuresData[ (featuresData.YEARWEEK >= 201601) &
                                (featuresData.YEARWEEK <= 201652)]

featuresData2016.head()


# In[15]:


#필요 라이브러리 정의
import matplotlib.pyplot as plt

# 커맨드뷰에서 차트 시연
get_ipython().run_line_magic('matplotlib', 'inline')
# 팝업 창 활용하여 차트 시연
x=featuresData2015[["WEEK"]]
y = featuresData2015[["QTY"]]
y2 = featuresData2016[["QTY"]]
# 차트 꾸미기, legend
plt.plot(x,y,"g", label="2015")
#plt.plot(x,y2,"bo--", label="2016")
plt.legend(loc=0)


# # 2. 데이터 시각화 고급

# In[ ]:





# In[11]:


#필요 라이브러리 정의
import matplotlib.pyplot as plt

# 팝업 창 활용하여 차트 시연
x=list(range(1,11,1))
y = [i**2 for i in x]
y2 = [i**2.2 for i in x]

# 서브플롯
fig = plt.figure(figsize=(10,4))
ax1 = fig.add_subplot(121)
ax1.plot(x,y, 'b',lw=1.5, label = '1st')

ax2 = fig.add_subplot(122)
ax2.plot(x,y2, 'g', lw=1.5, label='2nd')


# In[ ]:





# In[ ]:





# ### 1. 서브플롯 그리기

# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[11]:


#필요 라이브러리 정의
import matplotlib.pyplot as plt

# 팝업 창 활용하여 차트 시연
x=list(range(1,11,1))
y = [i**2 for i in x]
y2 = [i**2.2 for i in x]

# 서브플롯
fig = plt.figure(figsize=(10,10))
ax1 = fig.add_subplot(211)
ax1.plot(x,y, 'b',lw=1.5, label = '1st')
ax1.plot(x,y, 'o')
ax1.grid(True)
ax1.legend(loc=0)
ax1.set_xlabel('ax1_index')
ax1.set_ylabel('ax1_value')
ax1.set_title('subplot')
ax2 = fig.add_subplot(212)
ax2.plot(x,y2, 'g', lw=1.5, label='2nd')
ax2.plot(x,y2, 'go')
ax2.grid(True)
ax2.legend(loc=0)
ax2.set_xlabel('ax2_index')
ax2.set_ylabel('ax2_value')
ax2.set_title('ax2_title')


# ### 2. 이중축 활용하기

# In[3]:


import matplotlib
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 12}

matplotlib.rc('font', **font)
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


#필요 라이브러리 정의
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

# 팝업 창 활용하여 차트 시연
x=list(range(1,11,1))
y = [i**2 for i in x]
y2 = [i**2.2 for i in x]

# 이중축
fig = plt.figure(figsize=(10,8))
ax1 = fig.add_subplot(1,1,1)
#figure, ax1 = plt.subplots(figsize=(10,5))
ax1.plot(x,y, 'b--',lw=1.5, label = '1st')
ax1.plot(x,y, 'o')
ax1.grid(True)
ax1.legend(loc=0)
ax1.set_ylabel('ax1_value')
ax1.set_xlabel('ax1_index')
plt.title('subplot')
ax2 = ax1.twinx()
ax2.plot(x,y2, 'g', lw=1.5, label='2nd')
ax2.plot(x,y2, 'go')
ax2.legend(loc=0)
ax2.set_ylabel('ax2_value')


# In[17]:


#필요 라이브러리 정의
import matplotlib.pyplot as plt

# 팝업 창 활용하여 차트 시연
x=list(range(1,11,1))
y = [i**2 for i in x]
y2 = [i**2.2 for i in x]

# 이중축
fig = plt.figure(figsize=(10,5))
ax1 = fig.add_subplot(1,1,1)
#figure, ax1 = plt.subplots(figsize=(10,5))
plt.plot(x,y, 'b--',lw=1.5, label = '1st')
plt.plot(x,y, 'o')
plt.grid(True)
plt.legend(loc=0)
plt.ylabel('value')
plt.title('subplot')
ax2 = ax1.twinx()
plt.plot(x,y2, 'g', lw=1.5, label='2nd')
plt.plot(x,y2, 'go')
plt.legend(loc=0)
plt.xlabel('index')
plt.ylabel('value')


# ### 실습

# featuresData를 활용하여 
# 2015년도 자료만 활용하여
# x축: week 이중축으로 qty, pro_percent를 
# 차트로 그리세요
# 

# In[31]:


import pandas as pd

featuresData =  pd.read_csv("../dataset/feature_regression_example.csv")

featuresData2015 = featuresData[ (featuresData.YEARWEEK >= 201501) &
                                (featuresData.YEARWEEK <= 201552)]

featuresData2015.head()


# In[40]:


y2 = featuresData2015["PRO_PERCENT"]
print(type(y2))


# In[34]:


#필요 라이브러리 정의
import matplotlib.pyplot as plt

# 팝업 창 활용하여 차트 시연
x=featuresData2015[["WEEK"]]
y = featuresData2015["QTY"]
y2 = featuresData2015[["PRO_PERCENT"]]

# 이중축
fig = plt.figure(figsize=(10,5))
ax1 = fig.add_subplot(1,1,1)
plt.plot(x,y, 'bo--',lw=1.5, label = '1st')
plt.grid(True)
plt.legend(loc=2)
plt.ylabel('qty')
plt.title('subplot')
ax2 = ax1.twinx()
plt.plot(x,y2, 'g', lw=1.5, label='2nd')
plt.legend(loc=4)
plt.xlabel('week')
plt.ylabel('promotion')


# ### 차트종류 변경

# ### 차트 종류 변경하기

# In[20]:


#필요 라이브러리 정의
import matplotlib.pyplot as plt

x=list(range(1,11,1))
y = [i**2 for i in x]

plt.figure(figsize=(7,5))

plt.title('Scatter plt')
plt.scatter(x,y,marker='o', edgecolors='b')


# ### 차원추가 (Scatter 차트)

# In[41]:


#필요 라이브러리 정의
import matplotlib.pyplot as plt
import numpy as np

x=list(range(1,11,1))
y = [i**2 for i in x]
c= np.random.randint(0,3,len(y))

plt.figure(figsize=(7,5))
plt.scatter(x,y,marker='o',c=c)
plt.colorbar()

plt.title('Scatter plt')


# # 3. Seaborn

# In[50]:


# library & dataset
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[64]:


import pandas as pd
customerData = pd.read_csv("../dataset/customerdata.csv")


# In[65]:


customerData["CAT_CUST"] = customerData.CUSTTYPE.astype("category").cat.codes


# In[66]:


customerData.head(2)


# In[67]:


customerData[["CUSTTYPE","CAT_CUST"]].drop_duplicates()


# In[68]:


# library & dataset
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
# Use the 'hue' argument to provide a factor variable
#hue='CUSTTYPE'
# fit_reg=False
sns.lmplot( x="DEVICECOUNT", y="AVERAGEPRICE", data=customerData,
           fit_reg=True, legend=False, hue="CUSTTYPE")
 
# Move the legend to an empty part of the plot

plt.legend(loc='lower right')


# In[ ]:


# library & dataset
import seaborn as sns
 
# Use the 'hue' argument to provide a factor variable
sns.lmplot( x="PRODUCTAGE", y="DEVICECOUNT", data=customerData, fit_reg=False, hue='CAT_CUST', legend=False)
 
# Move the legend to an empty part of the plot
plt.legend(loc='lower right')
plt.show()


# In[ ]:


# library & dataset
import seaborn as sns
df = sns.load_dataset('iris')
 
# Use the 'hue' argument to provide a factor variable
sns.lmplot( x="sepal_length", y="sepal_width", data=df, fit_reg=False, hue='species', legend=False)
 
# Move the legend to an empty part of the plot
plt.legend(loc='lower right')
plt.show()


# # 3. Seaborn

# In[14]:


#pip install seaborn
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')

tips = sns.load_dataset('tips')
tips.head(1)


# In[15]:


sns.countplot(x="day", data = tips)


# In[51]:


#pip install seasborn
import pandas as pd
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')

tips = sns.load_dataset('tips')
tips.head(2)


# In[52]:


tips.dtypes


# ### 1. Countplot 구현

# In[53]:


sns.countplot(x="day", data = tips)


# ### 2. Distplot 구현

# In[54]:


l = [1,2,3,1,2,3,2,3,4]
sns.distplot(l)


# In[16]:


#pip install seasborn
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')

tips = sns.load_dataset('tips')
tips.head()
sns.distplot(tips["total_bill"])


# ### 3. jointplot구현

# In[19]:


tips.head()


# In[24]:


groupKey = ["time"]


# In[27]:


tips.groupby(groupKey)[["total_bill"]].describe()


# In[ ]:





# In[17]:


sns.jointplot(x="total_bill", y = "tip", data = tips, kind='kde')


# ### 실습. customerData.csv 파일 활용하여 [DEVICECOUNT, PRODUCTAGE] 두개 컬럼에 대한  JointPlot을 구현하세요

# In[57]:


customerData = pd.read_csv("../dataset/customerdata.csv")
customerData.head(2)


# In[58]:


sns.jointplot(customerData.DEVICECOUNT, customerData.PRODUCTAGE)


# ### 4. pair plot

# In[62]:


sns.pairplot(tips)


# In[63]:


sns.pairplot(tips, hue = "sex")


# In[64]:


customerData = pd.read_csv("../dataset/customerdata.csv")
customerData.head(2)


# In[65]:


csColumns = ["PRODUCTAGE","AVERAGEPRICE","DEVICECOUNT","CUSTTYPE"]


# In[66]:


customerData2 = customerData[csColumns]


# In[136]:


sns.pairplot(customerData2,  hue="CUSTTYPE")


# ### 5. barplot 차트

# In[74]:


tips.groupby("time")[["total_bill"]].ipynb_checkpoints/


# In[84]:


aa = tips.groupby("time")[["total_bill"]].describe()
aa


# In[86]:


bb = aa.reset_index()
bb


# In[100]:


cc = bb.total_bill


# In[104]:


import math


# In[110]:


7.713882/math.sqrt(68)*1.96


# In[111]:


9.142029/math.sqrt(176)*1.96


# In[107]:


cc["error_bar"] = math.sqrt(cc.count)


# In[ ]:


bb[[bb.variable_1 = "count"]]


# In[ ]:





# In[68]:


sns.barplot(x='time', y='total_bill', data = tips)


# In[91]:


tips.groupby(["time"])["total_bill"].describe()


# ### 6. boxplot 구현`

# In[90]:


sns.boxplot(x='time', y='total_bill',data=tips)


# In[113]:


groupTips = tips.groupby(groupKey)[["total_bill"]].describe()
groupTips2 = groupTips.reset_index()
groupTips2


# In[135]:


pd.concat([groupTips2["time"], groupTips2["total_bill"]], axis=1)


# In[119]:


tips.corr()


# In[39]:


tc = tips.corr()
sns.heatmap(tc, annot = True)


# In[99]:


flights = sns.load_dataset('flights')
flights.head()


# In[100]:


flights = sns.load_dataset('flights')
fp = flights.pivot_table(index='month', columns='year', values = 'passengers')

fp.head()


# In[101]:


sns.heatmap(fp)


# In[123]:


sns.clustermap(fp)


# In[124]:


sns.lmplot(x='total_bill', y = 'tip', data = tips )
sns.lmplot(x='total_bill', y = 'tip', data = tips, hue = 'sex', markers = ['o','v'] )


# In[177]:


import pandas as pd

featuresData =  pd.read_csv("../dataset/feature_regression_example.csv")

featuresData2015 = featuresData[ (featuresData.YEARWEEK >= 201501) &
                                (featuresData.YEARWEEK <= 201552)]

featuresData2015.head()


# In[190]:


import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
# 커맨드뷰에서 차트 시여
sns.set(font_scale=2)
sns.set(rc={'axes.axisbelow': True,
 'axes.edgecolor': '.8',
 'axes.facecolor': 'white',
 'axes.grid': True,
 'axes.labelcolor': '.15',
 'axes.spines.bottom': True,
 'axes.spines.left': True,
 'axes.spines.right': True,
 'axes.spines.top': True,
 'figure.facecolor': 'white',
 'font.family': ['sans-serif'],
 'font.sans-serif': ['Arial',
  'DejaVu Sans',
  'Liberation Sans',
  'Bitstream Vera Sans',
  'sans-serif'],
 'grid.color': '.8',
 'grid.linestyle': '-',
 'image.cmap': 'rocket',
 'lines.solid_capstyle': 'round',
 'patch.edgecolor': 'w',
 'patch.force_edgecolor': True,
 'text.color': '.15',
 'xtick.bottom': False,
 'xtick.color': '.15',
 'xtick.direction': 'out',
 'xtick.top': False,
 'ytick.color': '.15',
 'ytick.direction': 'out',
 'ytick.left': False,
 'ytick.right': False})

# paper, talk, poster
sns.set_context("talk")
figure, ax1 = plt.subplots(figsize=(20,8))

ax1 = sns.lineplot( data=[featuresData.QTY])
ax2 = ax1.twinx()
ax2 = sns.lineplot( data=[featuresData.PRO_PERCENT] , style="choice")


# # 한글깨짐현상 가이드

# In[26]:


import matplotlib.pyplot as plt

font_name = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
matplotlib.rc('font', family=font_name)
print(font_name)


# In[7]:


import matplotlib as mpl


# In[5]:


import matplotlib


# In[21]:


mpl.rc('font', family='nanumgothic')
mpl.rc('axes', unicode_minus=False)


# In[22]:


import matplotlib.pyplot as plt


# In[23]:


x=[1,2,3,4]
y=[1,4,9,16]


# In[24]:


get_ipython().run_line_magic('matplotlib', 'inline')

