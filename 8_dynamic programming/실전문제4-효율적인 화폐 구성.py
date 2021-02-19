# n종류의 화폐
# 개수의 최소한 합으로 가치가 M원이 되도록

n, m = list(map(int,input().split()))

v = []
for i in range(n):
    v.append(int(input()))