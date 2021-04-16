#!/usr/bin/env python
# coding: utf-8

# ### 지역변수, 전역범수

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
    outVlaue = step3

    return outVlaue

test1 = 1.2323423342
test2 = 15.32432
test3 = 23432523.22222

roundFunction(test1)

