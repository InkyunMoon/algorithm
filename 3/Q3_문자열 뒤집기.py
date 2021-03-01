'''
문자열 S가 주어지면 연속된 하나 이상의 숫자들을 '뒤집기'를 통해,
모든 숫자를 같게 만든다.

아이디어1)
주어진 문자열에서 0과 1중, 더 적은 숫자를 찾아 뒤집는다.

아이디어2)
'덩어리'가 더 적은 것을 찾는다.
------------------------------------------------
(풀이 참고한 뒤)
생각하지 못한 것
- 0과 1로 바꾸는 경우 각각을 count한 뒤 작은 것을 비교할 생각을 하지 못함
- '덩어리'를 처리하는 경우, 다음 숫자가 현재와 다른 경우에 덩어리였음을 파악하지 못함
    - 시작, 끝의 인덱스를 각각 찾아서 처리하려하는 등 복잡하게 생각함
'''
# 나의 풀이(2회)
str_ = input()
str_ = '0011010100001'
cnt0 = 0
cnt1 = 0

if str_[0] == '0':
    cnt1 += 1
else:
    cnt0 += 1

for i in range(len(str_) - 1):
    if str_[i] != str_[i+1]:
        if str_[i+1] == '0':
            cnt1 += 1
        else:
            cnt0 += 1

print(min(cnt0, cnt1))

### 풀이

data = input()
count0 = 0
count1 = 0

if data[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(data) -1):
    if data[i] != data[i+1]: # 이어지는 원소가 바뀌는 경우에만 처리해주도록 한다.
        if data[i+1] == '1':
            count0 += 1
        else:
            count1 += 1
print(count0, count1)