n = int(input())
movelist = input().split()
x = 1
y = 1

dx = [0, 0, -1 ,1]
dy = [-1, 1, 0, 0 ]
move = ['L', 'R', 'U', 'D']
for plan in movelist:
    for i in range(len(move)):
        if plan == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)




