'''
문자열 S가 주어지면 연속된 하나 이상의 숫자들을 '뒤집기'를 통해,
모든 숫자를 같게 만든다.

아이디어1)
주어진 문자열에서 0과 1중, 더 적은 숫자를 찾아 뒤집는다.

아이디어2)
'덩어리'가 더 적은 것을 찾는다.
'''

s = '0001100'

s_lst = list(map(int,s))

cnt_0 = s_lst.count(0)
cnt_1 = s_lst.count(1)
target = 1

def find_idx(lst, target):
    idx_lst = []
    for idx, val in enumerate(lst):
        if val == target:
            idx_lst.append(idx)
    return idx_lst

def flip(lst):
    if isinstance(lst,str):
        lst = list(map(int,lst))

    cnt_0 = s_lst.count(0)
    cnt_1 = s_lst.count(1)

    if cnt_0 < cnt_1: # 0의 수가 더 적으므로 0을 1로 바꿔야한다.
        for i in find_idx(lst, 0): # 0의 인덱스 위치를 찾아서
            lst[i] = 1 # 1로 바꾼다.
        return lst
    else:
        for i in find_idx(lst, 1):
            lst[i] = 0
        return lst

flip([1,1,1,1,1,1,1,0,1,0])