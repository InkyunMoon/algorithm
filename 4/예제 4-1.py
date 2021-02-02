#!/usr/bin/env python
# coding: utf-8

# In[54]:


# 4-1 상하좌우
N = int(input())
PLAN = list(input().split())


# In[59]:


x, y = 1, 1

for d in PLAN:
    if (d == 'R') and (y < N):
        y += 1
    elif (d == 'L') and (y > 1):
        y -= 1
    elif (d == 'U') and (1 < x <= N):
        x -= 1
    elif (d == 'D') and (1 <= x < N):
        x += 1 
    
print((x,y))


# In[60]:


# 답안지 풀이

x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D'] # x의 움직임은 '열'의 움직임이므로

for plan in PLAN:
    for i in range(len(move_types)): # 1번의 루프마다 4가지 중 하나의 움직임을 수행할 것이므로
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            
    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue # 공간을 벗어나는 경우는 무시하도록 한다.
        
    x, y = nx, ny # 공간을 벗어나지 않은 경우에 좌표를 업데이트한다.
    
print(x, y)


# In[ ]:




