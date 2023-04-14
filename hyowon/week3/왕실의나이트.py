# 4-3 왕실의 나이트
import sys

text = sys.stdin.readline()

x_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

x = text[0]
y = int(text[1])

x_loc = x_list.index(x) + 1

case = [[x_loc+1, y+2], [x_loc+1, y-2], [x_loc-1, y+2], [x_loc-1, y-2], [x_loc+2, y+1], [x_loc+2, y-1], [x_loc-2, y+1], [x_loc-2, y-1]]

cnt = 0
for i, j in case:
    if (1 <= i and i <= 8) and (1 <= j and j <= 8):
        cnt += 1

print(cnt)




