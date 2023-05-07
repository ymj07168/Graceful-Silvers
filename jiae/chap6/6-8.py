# 성적인 낮은 순서로 학생 출력하기

# 학생 수 입력받기
N = 2

# 학생 정보 입력받기
array = []
for _ in range(N):
  input_data = input().split()
  array.append((input_data[0], int(input_data[1])))

# 키를 이용하여, 점수를 기준으로 정렬
array = sorted(array, key=lambda student:student[1])

print(array)