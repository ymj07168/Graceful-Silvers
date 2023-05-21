# 재귀적으로 구현한 피보나치 수열(Top-Down DP)

# 한 번 계산된 결과를 Memoization하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수를 재귀함수로 구현
def fibo(x):
  # 종료조건(1 또는 2일때 1을 반환)
  if x == 1 or x == 2:
    return 1
  
  # 이미 계산한 적 있는 문제라면 그대로 반환
  if d[x] != 0:
    return d[x]
  
  # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
  d[x] = fibo(x-1) + fibo(x-2)
  return d[x]

print(fibo(9))