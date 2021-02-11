# n명의 학생 정보 존재
# 정보는 이름과 성적으로 구분
# 성적이 낮은 순서대로 학생의 이름을 출력

n = int(input('학생의 수를 입력하세요:'))

# 학생의 이름을 나타내는 문자열과 성적을 나타내는 정수가 공백으로 구분되어 입력된다.

name_grade = []
for _ in range(n):
    info = input().split()
    info[1] = int(info[1])
    name_grade.append([info[0], info[1]])

sorted_name_grade = sorted(name_grade, key = lambda x: x[1], reverse = False)

for i in range(len(sorted_name_grade)):
    print(sorted_name_grade[i][0], end = ' ')