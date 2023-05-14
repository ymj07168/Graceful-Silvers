N, K = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

#오름차순 정렬
a.sort()
b.sort(reverse=True)

for i in range(K):
    #a가 b보다 작으면 바꿈
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))
