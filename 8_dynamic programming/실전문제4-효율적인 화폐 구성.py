# n종류의 화폐
# 개수의 최소한 합으로 가치가 M원이 되도록

n, m = list(map(int,input().split()))
# n, m = 2, 15

array = []
for i in range(n):
    array.append(int(input()))

d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1): # j는 각 화폐를 나타낸다.
        # j == 15까지 반복문 수행
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j-array[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])