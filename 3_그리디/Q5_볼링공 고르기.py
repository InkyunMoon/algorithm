'''
서로 무게가 다른 공을 고르는 상황
볼링공 n개, 공의 번호는 1번부터 순서대로 부여

같은 무게라도 다른 공으로 간주
볼링공의 무게는 1부터 m까지 자연수 형태

[1,3,2,3,2]일 때, 1번부터 5번까지 번호 부여
-> 두 사람이 볼링공을 고르는 경우의 수는 8가지

문제: n개의 공의 무게가 각각 주어질 때, 두 사람이 공을 고르는 경우의 수는?
'''

# 개수와 무게가 주어진다.
n, m = 5, 3
# 각 볼링공의 무게 n개가 자연수 형태로 주어진다.
balls = [1,3,2,3,2]
sample = [1,2,3,4,5]

result = []
for idx, ball1 in enumerate(balls):
    for ball2 in balls[idx:]:
        if ball1 != ball2:
            result.append([ball1,ball2])
print(len(result))