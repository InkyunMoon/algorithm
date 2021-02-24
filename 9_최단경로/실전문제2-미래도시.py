# 1~n번의 회사들이 존재, 서로 도로를 통해 연결 됨
# 판매원 A는 현재 1번 회사에 위치, X번 회사에 방문하여 물건 판매 예정

# 회사끼리는 1시간 거리로 모두 동일
# 1번 -> k번 -> x번 회사로 방문하는것이 목적

n, m = map(int,input().split())
INF = int(1e9)

graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(n+1):
    for b in range(n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+ graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print(-1)
else:
    print(distance)