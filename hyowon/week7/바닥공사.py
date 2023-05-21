# 바닥공사
# a(i) = a(i-1) + a(i-2) * 2
import sys

N = int(sys.stdin.readline())

d = [0] * 1001

d[1] = 1
d[2] = 3
for i in range(3, N+1):
    d[i] = (d[i-1] + 2 * d[i-2]) % 796796

print(d[N])