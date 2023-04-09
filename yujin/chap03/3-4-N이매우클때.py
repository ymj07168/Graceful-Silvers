n, k = map(int, input().split())
result = 0

while True:
    # N == K로 나누어 떨어지는 수가 될 때까지 1씩 빼기
    target = (n//k) * k # n에 포함되는 k로 나눠 떨어지는 수 target
    result += (n-target) # target을 제외한 1씩 더해야 하는 것 result에 저장
    n = target # n에서 1 빼는거는 위에서 체크 됐으니 나눠 떨어지는 것 세기 위해 target 넣음
    # N이 K보다 작을 때 (더이상 나누기x) 탈출
    if n<k:
        break
    # k로 나누기
    result +=1 # 나눈 만큼 더해
    n//=k

# 마지막으로 남은 수에 대해 1씩 빼기
result += (n-1)
print(result)