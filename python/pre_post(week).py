#!/usr/bin/env python
# coding: utf-8

# ### preweek 사용

# In[ ]:


# 라이브러리 불러오기
from isoweek import Week
# input 변수 지정
inputYearWeek=input() #
inputWeek=int(input())
# preWeek 함수로 정의 인덱스로 년도 및 주차 계산
def preWeek(inputYearWeek, inputWeek):
    #yearWeek = str(yearWeek)
    year = int(inputYearWeek[0:4])
    week1 = int(inputYearWeek[4:])
    calcWeek = week1 - inputWeek
   # 년도 몇주차 인지 자동계산 함수를 변수 maxWeek 담기
    maxWeek = Week.last_week_of_year(year).week
    # if 문으로 주차 계산
    if ( week1 > inputWeek) :      # 예) 2020.20(week1)>10(inputWeek) 그냥 빼기
        answerWeek1=str(int(inputYearWeek)-inputWeek)
        print(answerWeek1)
    while calcWeek <= 0:
        year = year - 1
        calcWeek = maxWeek + calcWeek
        if(calcWeek < 10):
            outValue = str(year) + "0" + str(calcWeek)
        else:
            outValue = str(year) + str(calcWeek)
    return outValue

preWeek(inputYearWeek, inputWeek)


# ### postweek 사용

# In[ ]:


def postWeek(yearWeek, postWeek):  #postWeek 이후 주차를 반환하는 함수
    from isoweek import Week
    yeardigit = -2
    inputYear = int(str(yearWeek)[:yeardigit]) #년도만 잘라서 저장
    inputWeek = int(str(yearWeek)[yeardigit:]) #주차만 잘라서 저장
    resultWeek = inputWeek + postWeek           #현 주차 + 뒤로 갈 주차 계산결과
    calcWeek = Week.last_week_of_year(inputYear).week
    
    while(resultWeek>calcWeek):       # 주차가 넘어간다면
        inputYear = inputYear+1    # 년도가 하나 늘어납니다
        calcWeek = Week.last_week_of_year(inputYear).week  #늘어난 년도의 총 주차수
        resultWeek = resultWeek - calcWeek
        #resultWeek 에서 총 주차를 빼줍니다
        #결과가 아직도 총 주차보다 크다면 작아질때까지계속 반복
    
#     if(resultWeek<10):
#         resultWeek = "0"+str(resultWeek) # 1자릿수면 앞에 0을 붙여줌 -> zfill()로 처리.
        
    result = str(inputYear)+str(resultWeek).zfill(2) #년도와 주차를 문자열로 더해서 출력
    
    return result

