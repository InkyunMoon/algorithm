n = int(input('수열에 속해 있는 수의 개수 입력:'))

array = []
for _ in range(n):
    array.append(int(input()))

array.sort(reverse=True)

for i in array:
    print(i, end = ' ')