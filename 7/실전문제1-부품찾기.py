# n개의 부품
# 각 부품은 정수의 고유번호
# m개의 부품 대량구매 요청 - m개의 견적서 필요
# 가게안에 모든 부품이 있는지 확인하는 프로그램 작성

'''
예)

n = 5
arr = [8, 3, 7, 9 ,2]
m = 3
request = [5, 7, 9]
'''
# 손님이 요청한 부품 순서대로 부품 확인해서 있으면 yes, 없으면 no출력

n = int(sys.stdin.readline().rstrip())
parts = list(map(int,input().split()))
m = int(sys.stdin.readline().rstrip())
requests = list(map(int,input().split()))

def b_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    
    if array[mid] == target:
        return mid
    
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

for request in requests:
    if request == b_search(parts, request, 0, n-1):
        print('yes')
    else:
        print('no')