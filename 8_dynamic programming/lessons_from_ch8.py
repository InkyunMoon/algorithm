'''
p215
탑다운 - 메모이제이션(이전에 계산된 결과를 일시적으로 기록해 놓는 넓은 개념, 저장되어 다시 사용되지 않을수도 있다.)
바텀업 - DP테이블(결과 저장용 리스트)

p216
시스템상 재귀 함수의 스택 크기가 한정되어 있을 수 있기 때문에 탑다운 방식보다는 바텀업 방식으로 구현하는 것이 좋다.
recursion depth관련 오류가 발생하는 경우, sys라이브러리에 포함되어있는 setrecursionlimit() 함수를 호출하여 제귀 제한을 완화할 수 있다.

p223
d[i]에 속하는 값의 의미는 'i번째까지 처리했을 때 가능한 경우의 수'를 의미하는 듯...
'''