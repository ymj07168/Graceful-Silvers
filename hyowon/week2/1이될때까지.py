# 그리디 3-3
# 1이 될 때까지
import sys

N, K = map(int, sys.stdin.readline().split())

cnt = 0
while True:
    if N == 1:
        break

    if N % K == 0:
        N /= K
        cnt += 1

    else:
        N -= 1
        cnt += 1

print(cnt)