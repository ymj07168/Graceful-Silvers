# 개미전사

# 잘못된 내 풀이
# 1, 3, 1 이 있을 경우 3이 아닌 2를 출력

import sys

N = int(sys.stdin.readline())

food = list(map(int, sys.stdin.readline().split()))

d = [0] * 100
d[0] = food[0]
d[1] = food[1]
for i in range(2, N):


    d[i] = max(d[0:i-1]) + food[i]
    print(d[i])


print(max(d[:]))


# 답안 예시
d[0] = food[0]
d[1] = food[1]
for i in range(2, N):
    d[i] = max(d[i-1], d[i-2] + food[i])

print(d[N-1])