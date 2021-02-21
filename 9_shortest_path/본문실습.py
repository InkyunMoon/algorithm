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