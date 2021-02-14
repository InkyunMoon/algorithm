# 7-1 순차탐색

def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1

print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요" )

input_data = input().split()
n = int(input_data[0])
target = input_data[1]

array = input().split()

print(sequential_search(n, target, array))

# 7-2 이진 탐색을 재귀함수로 구현하기

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)
    
n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)

if result == None:
    print('원소가 존재하지 않습니다.')

else:
    print(result + 1 )