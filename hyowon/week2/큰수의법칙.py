# 큰 수의 법칙
import sys

N, M, K = map(int, sys.stdin.readline().split())
T = input().split()

for i in range(len(T)):
    T[i] = int(T[i])

T_sorted = sorted(T)

sum = 0
index = -1
cnt = 0
for i in range(M):
    sum += T_sorted[index]

    if index == -1:
        cnt += 1
    else:
        index = -1

    if cnt == K:
        index = -2
        cnt = 0

print(sum)



# 5 8 3
# 2 4 5 4 6