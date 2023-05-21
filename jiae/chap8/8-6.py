# 개미 전사

n = int(input())   # 정수 n 입력받기
arr = list(map(int, input().split()))  # 모든 식량 정보 입력받기

d = [0] * 100  # 앞서 계산된 결과를 저장하기 위한 dp 테이블 초기화

# 다이나믹 프로그래밍 진행(bottom-up)
d[0] = arr[0]
d[1] = max(arr[0], arr[1])
for i in range(2, n):
  d[i] = max(arr[i-2] + arr[i], arr[i-1])
  
print(d[n-1])