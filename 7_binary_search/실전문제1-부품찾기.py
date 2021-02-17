# n개의 부품
# 각 부품은 정수의 고유번호
# m개의 부품 대량구매 요청 - m개의 견적서 필요
# 가게안에 모든 부품이 있는지 확인하는 프로그램 작성

'''
예)

n = 5
parts = [8, 3, 7, 9 ,2]
m = 3
requests = [5, 7, 9]
'''
# 손님이 요청한 부품 순서대로 부품 확인해서 있으면 yes, 없으면 no출력

# 재귀함수로 풀어보기
import sys

n = int(sys.stdin.readline().rstrip())
parts = list(map(int,input().split()))
m = int(sys.stdin.readline().rstrip())
requests = list(map(int,input().split()))

def b_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    arr.sort()
    if arr[mid] == target:
        return mid
    
    elif arr[mid] > target:
        return b_search(arr, target, start, mid - 1)
    else:
        return b_search(arr, target, mid + 1, end)

for target in requests:
    result = b_search(parts, target, 0, n-1)
    if result == None:
        print('no', end = ' ')
    else:
        print('yes', end = ' ')

# 반복문으로 풀어보기
def b_search2(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for target2 in requests:

    result2 = b_search2(parts, target2, 0, n-1)
    if result2 == None:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')

        