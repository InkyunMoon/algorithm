# 10-4 서로소 집합을 활용한 사이클 판별 코드
## 서로소 집합은 "무방향 그래프" 내에서 사이클을 판별하기 위해 사용 가능

def find_parent(parent,x):
    # x번째 원소 != x번의 루트노드라면, x번째 원소와 x번의 루트노드가 같을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a): # a원소가 속한 루트노드를 찾아서(루트노드는 a로 초기화)
    b = find_parent(parent, b):
    if a < b:
        parent[b] = parent[a] # 큰 루트노드의 원소를 작은 루트노드의 원소로 치환
    else:
        parent[a] = perent[b]

# 노드의 개수와 간선의 개수 입력
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블의 원소를 모두 0으로 초기화

# 부모 테이블 내에서 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

cycle = False # 사이클 발생 여부

for i in range(e):
    a, b = map(int, input().split())
    # 사이클이 발생한 경우 종료
    
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else: # 싸이클이 발생하지 않은 경우
        union_parent(parent, a, b)
        
if cycle:
    print('싸이클이 발생하지 않았습니다.')
else:
    print('사이클이 발생하지 않았습니다.')


# 크루스칼 알고리즘 - 최단 신장트리 찾기

def find_parent(parent, x): # 루트노드를 찾는다.
    if parent[x] != 'x':
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b): # 두 원소가 속한 집합을 합치는 함수
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v+1) # 부모 테이블 초기화하기

# 모든 간선을 담을 리스트, 최종 비용을 담을 결과변수
edges = []
result = 0

# 부모테이블을 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# 모든 간선에 대한 정보 입력받기(간선의 개수만큼 반복문)
# (비용, 간선1, 간선2)의 튜플로 정보를 입력받는다. 튜플에서는 처음의 원소를 기준으로 정렬하게 된다.
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬한다.
edges.sort()

for edge in edges: # 간선을 하나씩 확인하며
    cost, a, b = edge # 간선의 원소들을 각각 다루기 위해
    # 사이클이 발생하지 않는 경우(루트노드가 서로 다른 경우)
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b) # 집합으로 묶어준다.
        result += cost # 현재 간선의 코스트를 결과에 더해준다.

print(result)

# 위상정렬
from collections import deque

v, e = map(int, input().split())

indegree = [0] * (v+1)

# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(v+1)]

# 방향 그래프의 모든 간선정보를 입력받기
for _ in range(g):
    a, b = map(int, input().split()) # a, b를 입력받아
    graph[a].append(b) # a에서 b로 입력이 가능하다는 의미로 사용한다.
    indegree[b] += 1 # 진입 차수를 1 증가시킨다.

def topology_sort():
    result = [] # 알고리즘 수행 결과를 담는 리스트
    q = deque() # 큐 기능으로 위상정렬을 수행할 것이므로 deque라이브러리 사용

    for i in range(1, v+1): # 모든 노드에 대해서
        if indegree[i] == 0: # 진입차수가 0인 노드를
            q.append(i) # 큐에 삽입한다.
    # 큐에 삽입된 원소가 모두 소진될 때 까지
    while q:
        now = q.popleft() # 큐에서 원소를 꺼내어
        result.append(now)

        # 꺼낸 원소와 연결된 노드들의 진입차수에서 1을 뺀다.
        for i in range[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입한다.
            if indegree[i] == 0:
                q.append(i)
    # 위상 정렬을 수행한 결과를 출력한다.
    for i in result:
        print(i, end= ' ')

topology_sort()