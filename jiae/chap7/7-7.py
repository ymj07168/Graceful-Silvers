# 부품 찾기(집합 자료형)

# 가게의 부품 개수(n) 입력받기
n = int(input())
# 가게에 있는 부품 번호를 입력받아서 집합(set) 자료형에 기록
array = set(map(int, input().split()))

# 손님이 확인 요청한 부품 개수(m) 입력받기
n = int(input())
# 손님이 확인 요청한 부품 번호 입력받기
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
  if i in array:
    print("yes", end=' ')
  else:
    print("no", end=' ')