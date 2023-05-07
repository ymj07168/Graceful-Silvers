n = int(input())
# 학생정보 = 학생 이름, 학생 성적
# 성적 낮은 순서대로 학생 이름 출력
students = []
for i in range(n):
    name, score = map(str, input().split())
    students.append([name, int(score)])
students.sort(key= lambda x : x[1]) # 두번째 요소 기준으로 정렬
for student in students:
    print(student[0], end=" ")
