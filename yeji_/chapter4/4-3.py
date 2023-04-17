now = input()
row = int(now[1])
column = ord(now[0]) - 96   #ord[a] 가 97이여서 96을 뺴줌..

steps = [(-2, -1), (-2, 1), (2, 1), (2, -1), (-1, -2), (1, -2), (-1, 2), (1, 2)]

count = 0
for step in steps:
    next_column = column + step[0]
    next_row = row + step[1]
    if next_column > 1 and next_row  > 1 and next_column <= 8 and next_row <= 8:
        count +=1


print(count)