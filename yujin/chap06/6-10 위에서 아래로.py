n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
# 내림차순 출력
arr.sort(reverse=True)
print(*arr) # 리스트 요소 한번에 출력하는 방법