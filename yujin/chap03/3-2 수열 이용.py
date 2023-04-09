# 입력
#5 8 3
#2 4 5 4 6
# 출력
#46

# 수열 사용해서 시간초과 막기
N, M, K = map(int, input().split())
num_list = list(map(int, input().split()))

num_list.sort(reverse=True)
max1 = num_list[0]
max2 = num_list[1]

max1_add_count = int(M/(K+1)) * K # 수열 뭉텅이로 M에서 나누면 몇뭉텅이인지 나오고 뭉텅이 별 K번
max1_add_count += M % (K+1) # (k+1)로 나눠 떨어지지 않으면 남은건 걍 더해버리면 됨

result = 0
result += max1_add_count * max1 #가장 큰 수 더하기
result += (M-max1_add_count) * max2 # 다음으로 큰 수 더하기

print(result)
