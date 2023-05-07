# 성적이 낮은 순서로 학생 출력하기
import sys

N = int(input())

student = []
for i in range(N):
    name, score = sys.stdin.readline().split()
    score = int(score)
    student.append([name, score])

student.sort(key=lambda x: x[1])

for n, s in student:
    print(n, end=' ')

