# 두 배열의 원소 교체
import sys

N, K = map(int, sys.stdin.readline().split())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A.sort()
B.sort(reverse=True)

# 바꾸기
for i in range(K):
    A[i] = B[i]

# 더하기
sum = 0
for a in A:
    sum += a

print(sum)