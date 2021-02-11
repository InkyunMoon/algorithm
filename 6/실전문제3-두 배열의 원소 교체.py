# 두 배열 A, B 존재
# 각 배열은 n개의 원소로 구성, 모두 자연수
# k번의 바꿔치기 연산 수행 가능 - A와 B의 원소 하나씩 골라 바꾸는 것
# 목표: 배열A의 모든 원소의 합이 최대

n, k = map(int, input().split())

arrays = []
for _ in range(2):
    temp = list(map(int, input().split()))
    arrays.append(temp)

for _ in range(k):
    min_1 = arrays[0].index(min(arrays[0]))
    max_2 = arrays[1].index(max(arrays[1]))

    if arrays[0][min_1] < arrays[1][max_2]:
        arrays[0][min_1], arrays[1][max_2] = arrays[1][max_2], arrays[0][min_1]

print(sum(arrays[0]))

# 교재 아이디어대로 다시 풀어보기

n, k = map(int, input().split())

arrays = []
for _ in range(2):
    temp = list(map(int, input().split()))
    arrays.append(temp)

arrays[0].sort()
arrays[1].sort(reverse = True)

for i in range(k):
    if arrays[0][i] < arrays[1][i]:
        arrays[0][i], arrays[1][i] = arrays[1][i], arrays[0][i]
    else:
        break

print(sum(arrays[0]))