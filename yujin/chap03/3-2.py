# 입력
# N M K
# N개의 자연수 공백 주어짐 1~10000수

# N : 2~1000 / M: 1 ~ 10000 / K:1~10000
# K <= M

# 출력 조건: 동빈's 큰수법칙 더한 값

N, M, K = map(int,  input().split())

num_list = list(map(int, input().split()))
# N개라 했으니 잘라주겠음
num_list = num_list[:N]

num_list.sort(reverse=True) # 내림차순
max1 = num_list[0]
max2 = num_list[1]
sum = 0
max1_can_add = K
for i in range(M):
    # M번 더해 max1과 max2 바꿔가면서
    if max1_can_add>0:
        sum += max1
        max1_can_add-=1
    elif max1_can_add==0:
        sum += max2
        max1_can_add=K
print(sum)
#5 8 3
#2 4 5 4 6

#46