n = 5
coins = [3, 2, 1, 1, 9]

for i in sorted(coins):
    print(i)

'''
target(만들어내고자 하는 값)을 증가시키며 현재 동전으로 만들어낼 수 있는지 확인을 반복

현재 가지고있는 동전으로 target을 만들어내야 하므로 target+동전 단위 만큼 증가시킨다.
'''