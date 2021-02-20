n = int(input())
# n = 4

food = list(map(int,input().split()))
# food = [1,3,1,5]

food

'''
a_1 = 1
a_2 = 3
a_3 = a_1 + a_3
a_4 = a_2 + a_4

a_n = a_1 + a_3 + a_5 + ... + a_n (where n is odd number)
a_n = a_2 + a_4 + a_6 + ... + a_n (where n is even number)
'''

# food

def attack(n, food):
    total_odd = 0
    total_even = 0
    for i in range(1, n, 2):
        total_even += food[i]
    for i in range(0, n, 2):
        total_odd += food[i]
    return max(total_even, total_odd)
            
attack(4, food)
# 풀긴 풀었는데 DP가 아닌듯...
# 2칸 건너뛰는 경우 고려하지 않음

# 해설 풀이

n = int(input())
# n = 4
food = list(map(int,input()))
# food = [1,3,1,5]
'''
amount_n = max(amount_n-1, amount_n-2 + x_n)
'''

d = [0] * 100 # d[n]는 n번째 식량창고까지 갔을 때 얻을 수 있는 식량의 최대 수
d[0] = food[0]
d[1] = max(food[0], food[1]) 

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + food[i])

print(d[n-1])

# 0222 다시풀기

n = 4
foods = [1,3,1,5]
# 최소 한 칸 이상 떨어진 식량창고를 약탈해야 한다.

d = [0]*100

'''
일직선상의 식량창고 중, 왼쪽부터 식량창고를 약탈한다고 가정, 왼쪽부터 i번째 식량창고까지 도달했을 때 약탈한 음식의 최대값을
d[i]라고 하자.
food_i는 i번째 식량창고에 있는 음식의 양.
'''
d[0] = 1
d[1] = 3
d[2] = 3 # 3번째 식량창고

# a_n = max(a_n-1, a_n-2 + food_i)

for i in range(3, n):
    d[i] = max(d[i-1], d[i-2]+foods[i])
print(d[n-1])

