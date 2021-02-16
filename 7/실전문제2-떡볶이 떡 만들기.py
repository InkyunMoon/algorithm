# 절단기에 높이 h를 지정하여 떡을 절단
# 요청한 길이가 m일 때, 적어도 m만큼의 떡을 얻기 위해서 절단기에 설정할 수 있는 높이의 최댓값은?

import sys
n, m = map(int, input().split())
heights = list(map(int,input().split()))
'''
n, m = 4 6
heights = [19, 15, 10, 17]
'''

heights.sort()

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None