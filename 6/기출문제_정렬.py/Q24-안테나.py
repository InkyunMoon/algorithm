# 안테나로부터 모든 집까지의 거리 합이 최소가 되도록
# 안테나는 집에만 설치 가능
# 동일 위치에 여러개 집 존재 가능

n = int(input())
house = sorted(list(map(int, input().split())))

result = []
for idx, anthena_pos in enumerate(house):
    temp_result = 0
    for house_pos in house:
        temp_result += abs(anthena_pos-house_pos)
    result.append(temp_result)

print(house[result.index(min(result))])