import heapq

n, m, start = map(int, input().split()) # 도시의 개수, 통로의 개수, 메시지를 보내고자 하는 도시
INF = int(1e9)
graph = [[] for i in range(n+1)]

for _ in range(1, m+1):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

distance = [INF] * (n+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heap.heappush(q, (cost, i[0]))

dijkstra(start)

count = 0
max_distance = 0
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)
print(count - 1, max_distance)

'''
다익스트라 알고리즘
- 한 지점에서 특정 한 지점까지 최단 경로를 구해야 하는 경우

플로이드 워셜 알고리즘
- 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우
- O(N^3)의 복잡도를 가지며, 노드의 개수가 500개 이하로 구성되는 경우가 많다.
'''