x = int(input())

# db테이블 초기화
dp_table = [0] * 30001

for i in range(2, x+1):
    # 현재 수에서 1을 빼는 경우
    dp_table[i] = dp_table[i-1] + 1
    # 각각 나눠 떨어질 경우 
    if i % 2 == 0:
        dp_table[i] = min(dp_table[i], dp_table[i // 2] + 1)

    if i % 3 == 0:
        dp_table[i] = min(dp_table[i], dp_table[i // 3] + 1)

    if i % 5 == 0:
        dp_table[i] = min(dp_table[i], dp_table[i // 5] + 1)

print(dp_table[x])