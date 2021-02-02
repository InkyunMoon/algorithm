#!/usr/bin/env python
# coding: utf-8

# In[44]:


def balanced_(letters):
    cnt = 0
    for letter in range(len(letters)):
        if letter == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return i


# In[45]:


def right_(letters):
    cnt = 0
    for letter in letters:
        if letter == '(':
            cnt += 1
        else:
            if cnt == 0: # 0인 경우는 ()())에서 )가 처리되는 순간에는 cnt==0이기 때문에
                return False
            cnt -= 1
    return True            


# In[46]:


def solution(letters):
    answer = ''
    if len(letters) == 0:
        return answer

    idx = balanced_(letters)
    print(idx)
    u = letters[:idx+1]
    v = letters[idx+1:]
    print(u, v)

    if right_(u):
        answer = u + solution(v)
    else:
        anaswer = '('
        answer += solution(v)
        answer += ')'

        u = list(u[1:-1])

        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
            answer += "".join(u)
    return answer


# In[50]:


solution(')()')


# In[48]:


balanced_('))')


# In[ ]:




