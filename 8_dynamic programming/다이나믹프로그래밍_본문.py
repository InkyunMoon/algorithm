# 8-2 피보나치 수열 소스코드(재귀)

# 한 번 계산된 결과를 메모이제이션하기 위해 리스트를 초기화한다.
d = [0] * 100

# 피보나치 함수를 재귀함수로 구현(top-down)
def fibo(x):
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]

    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))

# 8-3 피보나치 수열 반복문으로 작성해보기
d = [0] * 100

def fibo2(x):
    print('f('+str(x)+')', end = ' ')
    if x in [1,2]:
        return 1

    if d[x] != 0:
        return d[x]

    d[x] = fibo2(x - 1) + fibo2(x - 2)
    return d[x]

fibo2(6)

