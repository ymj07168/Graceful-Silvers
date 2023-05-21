# 효율적인 화폐 구성
import sys

n, m = map(int, sys.stdin.readline().split())

n_coin = []
for i in range(n):
    n_coin.append(int(sys.stdin.readline()))

d = [10001] * (m+1)

d[0] = 0
for i in range(n):
    for j in range(n_coin[i], m+1):
        if d[j - n_coin[i]] != 10001:
            d[j] = min(d[j], d[j - n_coin[i]] + 1)

if d[m] == 10001:
    print(-1)

else:
    print(d[m])
