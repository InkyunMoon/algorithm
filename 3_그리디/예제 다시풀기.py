n, m = map(int, input().split())
nums = []

for _ in range(n):
    nums.append(map(int,input().split()))

min_temp = []
for num in nums:
    min_temp.append(min(num))

max(min_temp)

# 해설 참고 후 다시풀어보기

result = 0
for _ in range(n):
    data = list(map(int, input().split()))

    MIN = min(data)

    result = max(result, MIN)

print(result)

# 4번 다시풀기

n , k = 24, 5

cnt = 0
while True:
    if n == 1:
        break

    if n % 5 != 0:
        n -= 1
        cnt += 1
    else:
        n //= k
        cnt += 1

print(cnt)
