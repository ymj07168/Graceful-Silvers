# 큰 수의 법칙
# 배열로 주어진 수를 M번 더하여 가장 큰 수를 만든다. 단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과해 더해질 수 없다.

def max_num1():
  N, M, K = map(int, input().split())
  a = list(map(int, input().split()))

  a = sorted(a, reverse=True)
  first = a[0]
  second = a[1]

  i = 0  # 가장 큰 수를 연속 몇 번 더했는지 카운트
  result = 0

  for m in range(M):  # 주어진 수를 M번 더하기
    if i < K:         # 가장 큰 수를 K번 더하기
      result += first
      i += 1
    else:             # 두 번째로 큰 수를 한 번 더하기
      result += second
      i = 0           # 두 번째로 큰 수를 더했으므로 카운트 초기화
        
  return result
  
def max_num2():
  N, M, K = map(int, input().split())
  a = list(map(int, input().split()))

  a = sorted(a, reverse=True)
  first = a[0]
  second = a[1]
  
  sequence_sum = first * K + second   # 반복되는 수열의 합
  sequence_count = M // (K + 1)       # 수열 반복 횟수
  mod_count = M % (K + 1)             # 반복에 포함되지 않는 나머지 숫자의 개수
  
  result = sequence_sum * sequence_count + first * mod_count
  
  return result

print(max_num2())