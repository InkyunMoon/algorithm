'''
1. 다익스트라 알고리즘
- 특정 노드에서 출발하여 다른 노드로 가는 각각의 최단경로를 구해주는 알고리즘
- '음의 간선'이 없을 때 정상적으로 동작

파이썬의 heapq라이브러리는 원소로 튜플을 입력받으면 튜플의 첫 번째 원소를 기준으로 우선순위큐를 구성한다.
따라서, (거리, 노드번호)순으로 데이터를 구성해 우선순위 큐에 넣으면 거리순으로 정렬된다.
그러므로 거리가 가장 짧은 노드를 선택하기 위해서는 우선순위 큐에서 그냥 노드를 꺼내면 된다.
'''

# heap(최소 힙) 예제
import heapq

def heapsort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, value) # heappush를 통해 힙 자료구조에 데이터를 추가할 수 있다.
    
    for i in range(len(h)):
        result.append(headq.heappop(h)) # heappop을 통해 힙 자료구조에서 데이터를 추출할 수 있다. heap 자료구조는 가장 우선순위가 높은 원소부터 추출된다는 특징이 있다.
                                        # 현재는 최소힙(파이썬 heap의 기본형)이므로 가장 작은 원소부터 출력되어 result에는 오름차순으로 정렬될 것이다.
    return result

result = heqpsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

# 파이썬에서는 최대힙을 제공하지 않기 때문에 데이터를 힙에 넣기 전에 부호를 바꾸어 넣고, 꺼낼 때 다시 부호를 바꾸어 꺼내면 최대힙과 같은 효과를 얻을 수 있다.

def heapsort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, -value)

    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8])
print(result)