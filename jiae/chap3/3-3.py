# 숫자 카드 게임
# 각 행에서 가장 작은 수를 가진 카드를 뽑고, 그 중에서 가장 큰 수를 출력한다.

n, m = map(int, input().split())
c = []
for i in range(n):
  c.append(list(map(int, input().split())))

min_value = min(c[0])
for i in range(1, n):
  if min_value < min(c[i]):
    min_value = min(c[i])

print(min_value)