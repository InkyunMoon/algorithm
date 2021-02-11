# 210211 - 점수가 같은 상황에 다른 정렬 조건을 어떻게 추가하는지 감을 잡지 못하였다.



# n : 인원 수
# 국어 영어 수학 순으로 점수 입력
'''
1. 국어점수 내림차순
2. 국어점수 같으면 영어점수 오름차순
3. 국어 영어 같으면 수학점수 내림차순
4. 모든 점수 같으면 이름 오름차순(대문자가 먼저)
'''

n = int(input())

score_lst = []

for _ in range(n):
    temp = list(input().split())
    name = temp[0]
    scores = list(map(int, temp[1:]))
    temp = [name] + scores

    score_lst.append(temp)

# score_lst = [['Jungkyu', 50, 60, 100], ['Sangkeun', 80, 60, 50], ['Sunyoung', 80, 70, 100], ['Soong', 50, 60, 90], ['Haebin', 50, 60, 100], ['Sangsoo', 60, 80, 100], ['Donghyuk', 80, 60, 100], ['Sei', 70, 70, 70], ['Wonseob', 70, 70, 90], ['Sanghyun', 70, 70, 80], ['nsj', 80, 80, 80], ['Taewhan', 50, 60, 90]]

result = sorted(score_lst, key = lambda x: [-x[1],x[2],-x[3],x[0]])

for name in result:
    print(name[0])