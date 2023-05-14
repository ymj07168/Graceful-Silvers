# 부품 찾기(계수 정렬)

# 가게의 부품 개수(n) 입력받기
n = int(input())
array = [0] * 100001

# 가게에 있는 부품 번호 입력받기
for i in input().split():
  array[int(i)] = 1

# 손님이 확인 요청한 부품 개수(m) 입력받기
n = int(input())
# 손님이 확인 요청한 부품 번호 입력받기
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
  if array[i] == 1:
    print("yes", end=' ')
  else:
    print("no", end=' ')