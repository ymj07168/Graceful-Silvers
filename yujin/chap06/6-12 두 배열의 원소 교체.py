n, k = map(int, input().split())
# n개 요소 두 배열, 최대 k번 바꿔치기 가능 - 배열 a와 b 서로 바꿔치기
# 배열 A의 원소의 합의 최댓값
# A에서 작은거 B에서 큰거 찾아 교환
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort() # 작->큰 오름차순
b.sort(reverse = True) # 큰 -> 작 내림차순

for i in range(k):
    # 최대!!!!!k번 교환 가능
    # 최대 k번이라 꼭 k번을 교환할 필요가 없다!!!
    # a가 b보다 작은 경우에만 교환!!
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
print(sum(a))