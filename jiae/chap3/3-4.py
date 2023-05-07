# 1이 될 때까지
# 입력이 최대 100,000이므로 시간복잡도 O(NlogN)인 알고리즘으로 구성한다.

n, k = map(int, input().split())

def until_one1():
  count = 0
  while n != 1:
    count += 1
    if n % k == 0:
      n = n // k
    else:
      n = n - 1
      
  print(count)
  
def until_one2():          # n의 범위가 100억 이상일 때, 시간을 줄이는 방법
  count = 0
  while True:
    target = (n // k) * k  # target : n보다 작거나 같으면서 k로 나누어떨어지는 수
    count += (n - target)  # n이 k로 나누어떨어지는 수가 될때까지 1을 빼는 횟수만큼 증가
    n = target             # n은 k로 나누어떨어지는 수가 됨
    
    if n < k:              # n이 k보다 작아서 더 이상 나눌 수 없을 때 반복문 탈출
      break
    
    count += 1             # 연산(k로 나누기) 횟수 증가
    n //= k
  
  # 마지막으로 남은 수에 대해 1씩 빼기
  # 예) n = 8, k =4면 8 -> 4 -> 2여서 2를 1로 만들어줘야함
  count += (n - 1)
  print(count)