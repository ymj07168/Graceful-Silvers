# 1이 될 때까지
# 입력이 최대 100,000이므로 시간복잡도 O(NlogN)인 알고리즘으로 구성한다.

n, k = map(int, input().split())

count = 0
while n != 1:
  count += 1
  if n % k == 0:
    n = n // k
  else:
    n = n - 1
    
print(count)