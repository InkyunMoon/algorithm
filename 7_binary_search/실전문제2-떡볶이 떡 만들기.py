# 절단기에 높이 h를 지정하여 떡을 절단
# 요청한 길이가 m일 때, 적어도 m만큼의 떡을 얻기 위해서 절단기에 설정할 수 있는 높이의 최댓값은?

import sys
n, m = map(int, input().split())
heights = list(map(int,input().split()))
'''
n, m = 4, 6
heights = [19, 15, 10, 17]
'''

heights.sort()

start = 0
end = max(heights)

result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in heights:
        if x > mid:
            total += x - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)

# 시작점과 끝점 사이 중간지점을 떡을 자르는 위치로 설정
# 잘린 떡의 총합이 목표치보다 낮다면, 끝지점을 줄여서 중간지점을 왼쪽으로(떡을 더 자르게)
# 총합이 목표치보다 크다면, 시작지점을 mid+1로 설정해서 떡을 덜 자르게