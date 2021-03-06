'''
회전판에 n개의 음식 존재
1~n까지 번호

1번부터 섭취, 번호 순대로 음식이 앞에 놓여짐
마지막 번호 섭취 후 다시 1번 음식이 놓여짐
음식 하나를 1초동안 섭취 후 그대로 두고, 다음 음식(현재 음식에서 가장 가까운 번호) 섭취
회전판이 회전하는 시간은 없다고 가정

k초 후 방송 중단. 다시 방송 이어갈 때 몇 번 부터 먹어야 하는지 알고싶다.
'''

food_times = [3,1,2]
k = 5

def list_operation(lst, idx):
    if lst[idx] > 0:
        lst[idx] = lst[lst.index(lst[idx])]-1
        return lst
    else:
        return lst

def solution(k, food_times):
    count = 0
    idx_list = list(range(0,len(food_times)))
    for idx in [idx_list*k][0][:k+1]:
        food_times = list_operation(food_times,idx)
        count += 1
    return food_times, count
# 1초가 지날때마다 감소하는 food_times를 구했지만 섭취해야하는 음식의 번호를 리턴하지는 못함...
# 시간이 적게 걸리는 음식부터 제거한다?

'''
- k초 후에 먹어야 할 음식의 번호를 출력해야 한다. -> 음식의 번호도 함께 입력한다.
'''


import heapq

q = []
heapq.heappush(q, (0,2))

heapq.heappop(q)