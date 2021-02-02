#!/usr/bin/env python
# coding: utf-8

# In[10]:


n = int(input())


# In[11]:


cnt = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
             if '3' in str(i) + str(j) + str(k):
                    cnt += 1
                    
print(cnt)


# In[13]:


# 3이 들어간 숫자를 체크하는 방식에서 숫자를 문자열로 변환하여 인식한다는 아이디어를 떠올리지 못했다.


# In[ ]:




