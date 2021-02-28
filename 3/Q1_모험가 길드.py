'''
공포도가 낮은 경우, 적은 수의 사람으로 그룹을 결성할 수 있다. -> 그리디 문제임을 파악한다.
공포도가 낮은 사람부터 우선적으로 처리하도록 한다. 
예를들어, [2, 3, 1, 2, 2]와 같은 공포도 리스트 중 1인 사람은 혼자 그룹 결성 가능. 2인 사람 두명이서 그룹 결성 가능.
-> 공포도가 낮은 사람부터 우선 처리하여 그룹의 수를 최대화 시킨다.

언제까지 우선처리 할 것인가?
현재의 공포도보다 사람의 수가 적으면(공포도가 사람의 수보다 크면) 그룹을 결성할 수 없으므로 멈춘다.
즉, 현재의 공포도(fear)가 사람의 수보다 작거나 같으면 계속한다.(그룹에 사람을 추가한다.)
'''

n = int(input())
# fears = list(map(int,input().split()))
fears = [2,3,1,2,2]

no_adventurer = 0
no_group = 0

fears.sort() # [1,2,2,2,3]

for fear in fears:
    no_adventurer += 1
    if no_adventurer >= fear:
        no_group += 1
        no_adventurer = 0

print(no_group)