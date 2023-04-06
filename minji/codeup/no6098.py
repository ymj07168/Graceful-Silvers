miro = list()
for i in range(10):
    miro.append(list(map(int, input().split())))

x = 1
y = 1
miro[x][y] = 9
while True:
    if miro[x][y + 1] != 1:
        if miro[x][y + 1] == 2:
            miro[x][y + 1] = 9
            break
        miro[x][y + 1] = 9
        y += 1
    elif miro[x + 1][y] != 1:
        if miro[x + 1][y] == 2:
            miro[x + 1][y] = 9
            break
        miro[x + 1][y] = 9
        x += 1
    else:
        break

for i in range(10):
    for j in range(10):
        print(miro[i][j], end=' ')
    print()