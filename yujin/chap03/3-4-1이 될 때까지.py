# 4 1이 될 때까지
# N은 항상 K보다 크거나 같은 자연수
# 입력: N K
# 출력: 규칙 1, 2 수행 최소 횟수

n, k = map(int, input().split())
count = 0
while True:
    # 2번 규칙
    if n%k == 0:
        n//=k
    else:
        # 1번 규칙
        n -= 1
    count+=1
    if n == 1:
        print(count)
        break
