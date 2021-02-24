# DFS 메서드 정의

def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end = ' ')
    
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9


# In[17]:


dfs(graph, 1, visited)


# In[82]:


# BFS - 특정 조건에서의 최단경로 문제로 자주 활용되는 알고리즘
from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    
    # 현재 노드를 방문 처리
    visited[start] = True

    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end = ' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True       
                
visited = [False] * 9


# ## 실전문제 1 - 음료수 얼려먹기, p149
# 얼음 틀의 모양이 인접행렬로 나타내면 직관적일 것 같다.
n, m = map(int,input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int,input())))

# 아이스크림(이어진 얼음 구멍이 몇개인지?)의 개수를 구하는 문제이므로 DFS가 적합할 것 같다?
# 1인 경우는 탐색하지 않고 0인 경우만 탐색한다. -> 0인 경우 1을 더하여 방문처리하도록 한다.
# dfs이므로 재귀 형태를 띨 것인데, 멈춤 조건을 먼저 줘서 불필요한 진행을 미리 방지하자.

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False # 틀을 벗어난다면 False를 리턴한다.
            
    if graph[x][y] == 0: 
        graph[x][y] = 1 # 방문하지 않았다면 1로 초기화.
        
        for k in range(4): # 방문하지 않은 위치에서 상하좌우로 한번씩 가본다.
            nx = x + dx[k] # 가보면서 방문한 위치이면 False 리턴하고 멈출 것.
            ny = y + dy[k]
            dfs(nx,ny)
        return True # 상하좌우 다 돌면 True 리턴
    return False # 조건 벗어나지 않았지만 두번쨰 if문(방문 안했는지 여부)에 걸린다면 그대로 False리턴

num = 0
for i in range(n): # 4*5만큼 그리드를 움직이며 dfs를 수행.
    for j in range(m):
        if dfs(i,j) == True:
            num += 1 # depth끝까지 갔다면 +1한다.
print(num)

#-----#-----#-----#-----#-----#-----#
# 실전문제 2 - 미로탈출
# 동빈의 위치는 (1, 1), 미로의 출구는 (N, M). 즉, 가장 오른쪽 아래 위치

# 괴물이 있는 부분 0, 없는 부분 1이므로 없는 부분을 따라가야한다.
# 최소 이동 칸의 개수를 구한다.(미로는 N*M크기의 사각형, 한 칸은 동일하다고 가정) -> BFS로 풀 수 있겠다!
from collections import deque
# 최소 이동 칸의 개수를 구하는 문제이므로 한 칸씩 움직이며 BFS를 완전히 수행했을 때 cnt+1 해주면 되지 않을까?
n, m = map(int,input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = deque()
deque((1,2))
# queue.append((1,2))
queue

def bfs(x, y):
    queue = deque()
    queue.append((x, y)) # deque([(1, 2)])를 리턴. deque([1, 2])를 리턴하는 deque((x,y))와는 다름
    
    while queue:
        x, y = queue.popleft() # 가장 먼저 들어온 x, y를 선택, 해당 x, y에 연결된 노드들을 탐색
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
                        # x, y가 0미만일 수는 없다. 0일때 첫번째 인덱스인데, 그 미만은 미로를 벗어난다. -> 패스
                        # 가장 큰 행은  n-1행일 것. 
            if graph[nx][ny] == 0:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1 # 방문처리를 한다.(이전 값의 +1이므로 해당 위치가 몇번째 칸인지 나타낸다.)
                queue.append((nx,ny)) # 방금 방문한 좌표를 queue에 넣고 반복.
    return graph[n-1][m-1]

print(bfs(0,0))
# 실전문제 2 - 미로탈출 p152
from collections import deque

n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

# # 백준 2667, DFS & BFS로 풀어보기

# In[56]:


# 2667

cnt = 0 # 각 단지마다 집의 개수

MAP = []

n = int(input()) # 지도의 크기 n*n
for _ in range(n):
    MAP.append(list(map(int,input())))


# In[3]:


ANSWER = [] # 각 단지에 몇개의 아파트가 있는지 확인
visited = [[False] * n for _ in range(n)] # 방문 확인용


# In[4]:


dx = [-1, 1, 0, 0]
dy = [0, 0 , -1, 1]

def dfs(x, y):
    global cnt
    cnt += 1
    visited[x][y] == True
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < n:
            
            if MAP[nx][ny] == 1 and visited[nx][ny] == False:
                dfs(nx, ny)


# In[ ]:


for i in range(n):
    for j in range(n):
        if MAP[i][j] == 1 and visited[i][j] == False:
            cnt = 0
            dfs(i,j)
            ANSWER.append(cnt)
            
print(len(ANSWER))
ANSWER.sort()
print('\n'.join(map(str, ANSWER)))


# ### BFS로 풀어보기(보류)

# In[51]:


from collections import deque


# In[ ]:





# ## search problem - 연습문제

# ##### 15번 문제. 특정 거리의 도시 찾기
# 
# - N: 도시의 수
# - M: 단방향 도로 수
# - X: N개의 도시 중 특정된 도시
# - K: 지정된 최단 거리

# # Q
# - Q1. 1 -> 2 & 1 -> 3인 경우 2 -> 1 & 3 -> 1은 성립하지 않는가??
#        - 무향그래프의 경우 성립하지만, 현재는 '단방향'이라고 언급했으므로 성립X
# 
# - 인접 행렬 & 인접 리스트 방식 차이 ?

# In[315]:


n, m, k, x = map(int,input().split())

graph = [[] for _ in range(n+1)]


# In[316]:


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


# In[317]:


distance = [-1] * (N+1)
distance[x] = 0


# In[321]:


route[1]


# In[331]:


graph


# In[333]:


q = deque([x])
while q:
    now = q.popleft()
    
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)


# In[334]:


check = False

for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True
        
if check == False:
    print(-1)
