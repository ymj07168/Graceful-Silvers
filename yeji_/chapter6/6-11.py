n = int(input())
stlist = []

for i in range(n):
    st = input().split()
    #이름, 성적 순으로 저장 (성적은 정수형으로 변환하여 정렬)
    stlist.append((st[0], int(st[1])))


#점수를 기준으로 정렬(key lambda를 이용하여 정렬)
stlist = sorted(stlist, key=lambda student: student[1])

for student in stlist:
    print(student[0], end= " ")
