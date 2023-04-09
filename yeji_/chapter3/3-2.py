#내가 작성한 코드
N, M, K = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
first = data[N-1]
second = data[N-2]

#몫
count = M // (K +1)
#나머지
remainder = M % (K + 1)

result = ((first * K) + second) * count + first * remainder

print(result)



#-------------------------------------------------------------------------
#교제 해설_단순하게 푸는 답안 예시
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
first = data[N-1]
second = data[N-2]

result = 0

while True:
    for i in range(K):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)



#----------------------------------------------------------------------
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
first = data[N-1]
second = data[N-2]

count = int(m / (k +1)) * k
count += m % (k + 1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)