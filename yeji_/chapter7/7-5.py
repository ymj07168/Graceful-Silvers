n = int(input())
a = set(map(int, input().split()))
#list로 했는데 교제 답안에는 set으로 나와있음.
# => Set는 중복을 허용하지 않고 순서가 없지만, List는 중복을 허용하고 저장되는 순서가 유지된.

m = int(input())
b = list(map(int, input().split()))

for i in b:
    if i in a:
        print('yes', end=" ")
    else:
        print('no', end=" ")