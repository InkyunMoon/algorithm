# 아직 배우지 않은 '우선순위 큐'라는 개념이 나온다.
# 해당 개념을 공부하고 다시 돌아오기로 한다.

n = int(input())
n = 5
cards = []
for _ in range(n):
    cards.append(int(input()))

def no_compare(cards):
    cards.sort()

    temp = []
    for i in range(0, n):
        if i+2 < n:
            temp_sum = sum(cards[i:i+2])
            temp.append(temp_sum)
    return temp

list(range(0,3))
no_compare([10,20,30,40,50])