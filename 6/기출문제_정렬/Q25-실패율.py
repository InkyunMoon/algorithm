# 계수정렬로 푸는게 쉬울 듯?
# 계수정렬, 실패율 까지 계산하는데 성공, 그러나 스테이지의 번호를 실패율의 내림차순으로 정렬하는데 실패

import numpy as np

n = 5
example = [2,1,2,6,2,4,3,3]
example1 = [4,4,4,4,4]

def cnt_sort(example):
    unique_example = set(example)
    temp_cnt = np.zeros(max(unique_example)+1)
    for idx in unique_example:
        temp_cnt[idx] = example.count(idx)
    return temp_cnt

def solution(n, stage):
    result = []
    cnt = list(map(int,cnt_sort(stage)))
    for i in range(len(cnt)):
        result.append(cnt[i]/len(list(filter(lambda x: x>=i, stage))))
    
    return result[1:n+1]

a = solution(5, example)

sorted(a, reverse = True)

t = dict()
for idx, value in enumerate(sorted(a, reverse = True)):
    t[value] = idx+1

# 답지 보고 다시 풀어보기

def solution(n, stages):
    length = len(stages)
    answer = []
    for i in range(1, n+1):
        count = stages.count(i)

        if length == 0:
            fail = 0
        else:
            fail = count / length
        answer.append((i, fail))
        length -= count

    answer = sorted(answer, key = lambda x: x[1], reverse = True)

    return [i[0] for i in answer]

solution(5, example)