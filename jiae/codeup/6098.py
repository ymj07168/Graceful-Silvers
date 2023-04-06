a = [[]]
for i in range(10):
  row = list(map(int, input().split()))
  row.insert(0, 0)
  a.append(row)
x, y = 2, 2

while 1:
  if a[x][y] == 2:
    a[x][y] = 9
    break
  
  a[x][y] = 9
  if a[x][y+1] == 0:
    y += 1
  else:
    if x+1 == 10:
      if a[x][y+1] == 1:
        break
      else:
        y += 1
    else:
      x += 1

for i in range(1, 11):
  for j in range(1, 11):
    print(a[i][j], end=' ')
  print()
