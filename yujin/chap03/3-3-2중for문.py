n, m = map(int, input().spilt())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    ######
    # 현재 줄에서 가장 작은 수 찾기(min() 안 써서)
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    ########
    # 가장 작은 수들 중 가장 큰 수 찾기
    result = max(result, min_value) #얘는 2개씩 비교

print(result)