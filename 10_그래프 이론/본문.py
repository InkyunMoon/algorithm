# 10-4 서로소 집합을 활용한 사이클 판별 코드
## 서로소 집합은 무방향 그래프 내에서 사이클을 판별하기 위해 사용 가능

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
