'''
* 혹은 + 연산만을 사용해서 가장 큰 수를 구하는 프로그램 작성
-> 가장 큰 수를 구하는 것이므로 + 보다는 *를 우선적으로 사용할 필요성
0 or 1의 숫자는 더하기, 2이상의 숫자인 경우 곱하기 연산 적용
'''

nums = input()
sum_condition = [0, 1]
result = 0
cnt = 0
for num in map(int,nums):
    if cnt == 0 or result == 0:
        result += num
        cnt += 1
    else:
        if num in sum_condition:
            result += num
            cnt += 1
        else:
            result *= num
            cnt += 1

print(result)

