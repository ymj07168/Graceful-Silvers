# 그리디 3-3
# 숫자 카드 게임
import sys

N, M = map(int, sys.stdin.readline().split())


data = []

for i in range(N):
    m = list(map(int, sys.stdin.readline().split()))
    data.append(m)

m_min = []
for i in range(N):
    m_min.append(min(data[i]))

print(m_min)
n_m_max = max(m_min)
print(n_m_max)

