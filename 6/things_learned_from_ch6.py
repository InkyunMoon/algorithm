'''
6-1_선택정렬) 스와프
한 리스트에서 두 인덱스간의 자리를 바꿀 때,
1) array[i] = array[min_index]
   array[min_index] = array[i] 와 같은 방법으로 시행하면 제대로 바뀌지 않는다.

2) array[i], array[min_index] = array[min_index], array[i] 와 같은 방법으로 시행해야한다.
----------------------------------------------------------------------------------

p 176
- sorted(list) : 정렬된 list를 리턴
- list.sort() : 결과를 리턴하지 않고 list를 정렬

p 359 - 24번 실전문제
- sorted의 Key 인자로 리스트 형태를 주어 정렬의 우선순위를 설정할 수 있다.
'''