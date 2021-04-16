#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
# random으로 randint 함수를 통해 1~20까지의 배열과 size=20의 값을 생성
arr = np.random.randint(1, 20, size=20)

arr
# 생성된 배열을 버플정렬
for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if (arr[i] < arr[j]):
            arr1=arr[i];	
            arr[i]=arr[j]; 
            arr[j]=arr1;

print(arr)

