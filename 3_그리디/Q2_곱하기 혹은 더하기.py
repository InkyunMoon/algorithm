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


# 210307 - 2회차 풀이
'''
문자열 S가 주어짐
* 혹은 + 연산자를 넣어 만들 수 있는 큰 수를 구한다.
모든 연산은 왼쪽에서부터 순서대로 이루어진다.

아이디어)
- 0 혹은 1인 경우, 곱하는 것 보다 더하는 쪽이 수를 더 크게 한다.
- 맨 앞자리 수가 0인 경우, 다음 수를 반드시 더해야한다.
- 더한 수가 1인경우에는 다음 숫자를 곱하기보다 더해야 더 커진다. -> 결과적으로 다 같은말이네...
    예) 1 * 8 = 8
        1 + 8 = 9
'''

nums = '567'

result = 0
op= int(nums[0])

for num in nums[1:]:
    num = int(num)
    
    if op <= 0:
        op += num
    else:
        op *= num
    
print(op)