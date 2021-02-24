# 9-1 간단한 다익스트라 알고리즘 O(V^2)의 복잡도, V=노드 개수

import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split()) # 노드의 개수, 간선의 개수
start = int(input()) # 시작 노드번호
graph = [[] for i in range(n+1)] # 각 노드에 연결되어있는 노드들에 대한 정보를 담는 리스트
visited = [False] * (n+1) # 방문여부 체크 리스트
distance = [INF] * (n+1) # 최단거리 테이블을 모두 무한으로 초기화

for _ in range(m):
    a, b, c = map(int, input().split()) # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))

def get_smallest_node():
    min_value = INF
    index = 0

    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1] # ex) j == [(2,2), (3,5), (4,1)]이므로 j[0] == (2,2)
        # distance[j[0]] == graph[1][0][0] == 2가 될 것.
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True

        for j in graph[now]:
            cost = distance[now] + j[1]

            if cost < distance[j[0]]:
                distance[j[0]] = cost
dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print('INFINITY')

    else:
        print(distance[i])

# 9-2 개선된 다익스트라 알고리즘 소스코드
import heapq
import sys

input = sys.stdin.readline
INF = int(ie9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # q라는 힙에 (거리:0, 시작지점:start)인 튜플을 삽입. 출발노드로 가는 거리를 0으로 설정해서 우선순위큐에 넣어준다.
    distance[start] = 0 # 시작지점으로까지의 거리는 0으로 초기화. 출발노드(start)로 가는 거리를 0으로 설정하고 큐에 넣도록 한다.
    while q: # 우선순위 큐가 빌 때까지 데이터를 하나씩 꺼내서 처리하도록 한다.
        dist, now = heapq.heappop(q) # 거리, 현재 지점을 꺼낸다. dist가 작은 순서부터 우선하여 꺼내진다.
        if distance[now] < dist: # 현재 노드로 가는 거리가 최단거리테이블의 거리보다 작으면 무시한다. 꺼내진 노드가 현재 거리보다 작으면 (처리된 것으로 간주하고)무시하도록 한다.
            # dist는 현재 꺼낸 노드에서 특정 인접노드로 가는 거리
            continue
        # 현재 노드와 인접한 노드들 확인
        for i in graph[now]: # 현재 꺼낸 노드까지 도달하는 거리 + 인접한 노드들까지 가는 거리. 현재 꺼낸 노드에 대해서 그 노드를 거쳐가는 경우를 고려하도록 한다.
            cost = dist + i[1] # i[1]는 현재 꺼낸 노드와 인접한 노드의 거리를 의미한다.
            # i는 현재 노드 now로부터 (인접노드, 가는 비용)으로 구성되어있다.
            if cost < distance[i[0]]: # 현재 노드를 거쳐서 다른노드로 이동하는 거리가 짧은 경우에 다음의 코드 실행
                distance[i[0]] = cost # 그 작은 비용으로 갱신한다.
                # 즉, 그렇게 구한 거리가 인접한 노드까지의 최단거리보다 짧으면 최단거리 테이블을 갱신한다.
                heapq.heappush(q, (cost, i[0])) # 그럴 때마다 우선순위큐에 해당 정보가 기록되도록 한다.
                # 다시말해, 우선순위 큐에 해당 노드로 가는 비용을 업데이트하는 것.
dijkstra(start)

for i in range(1, n+1): # 모든 노드로 가기 위한 최단 거리 출력
    if distance[i] == INF:
        print('INFINITY') # 도달할 수 없는 경우, 무한으로 출력
    else:
        print(distance[i]) # 도달할 수 있는 경우, 거리를 출력


# 플로이드 워셜 알고리즘

INF = int(1e9) # 무한을 10억으로 설정한다.

n = int(input()) # 노드의 개수
m = int(input()) # 간선의 개수를 입력받는다.

# 노드가 1번부터 출발한다고 가정, n+1만큼 각각의 행과 열을 구성, 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자신으로 가는 비용(대각선의 값)은 모두 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# a노드에서 b노드로 가는 비용이 c라고 설정하여 graph를 구성한다.
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 3중 반복문을 통해 모든 노드에서 다른 모든 노드로까지의 최단거리를 구할 수 있다.
for k in range(1, n+1): # k는 거쳐가는 노드
    for a in range(1, n+1): # 출발노드
        for b in range(1, n+1): # 도착노드
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF: # a에서 b로 도달할 수 없는 경우, '무한'출력
            print('infinity', end = ' ')
        else: # 도달할 수 있다면, 그 거리를 출력한다.
            print(graph[a][b], end = ' ')
    print()