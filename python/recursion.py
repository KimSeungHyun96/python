#!/usr/bin/env python
# coding: utf-8

# ### 재귀함수

# In[1]:


def HelloWorld(n):
    if n >= 5:
        return 5
    else:
        return n * HelloWorld(n + 1)

HelloWorld(1)


# In[2]:


def HelloWorld(n):
    if n >= 200:
        return 200
    else:
        return n + HelloWorld(n + 1)

HelloWorld(100)


# ### 피보나치

# In[3]:


def HelloWorld(n):
    if n <= 1:
        return n
    else:
        return HelloWorld(n - 1) + HelloWorld(n - 2)

HelloWorld(10)

