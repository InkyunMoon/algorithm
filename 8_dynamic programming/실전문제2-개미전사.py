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