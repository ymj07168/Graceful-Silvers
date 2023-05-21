# 효율적인 화폐 구성

n, m = map(int, input().split())

# n개의 화폐 단위 정보를 입력받기
arr = []
for _ in range(n):
  arr.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 dp 테이블 초기화
d = [10001] * (m + 1)
d[0] = 0

# bottom-up 방식으로 dp 진행
for i in range(n):  # 화폐 단위별로 만들 수 있는 금액인지 계산
  for j in range(arr[i], m + 1): 
    if d[j - arr[i]] != 10001:  # (i - k)원을 만드는 방법이 존재하는 경우
      d[j] = min(d[j], d[j - arr[i]] + 1)

# 계산된 결과 출력
if d[m] == 10001:  # m원을 만드는 방법이 없는 경우
  print(-1)
else:
  print(d[m])