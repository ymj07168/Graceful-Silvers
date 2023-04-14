# 상하좌우
import sys

N = map(int, sys.stdin.readline().split())
command = list(sys.stdin.readline().split())

# 초기 좌표
global x, y
x = 1
y = 1

# (x, y) x: 위아래, y:좌우
def move(c):
    global x, y
    if c == 'R' and y+1 <= 5:
        y += 1
    elif c == 'L' and y-1 >= 1:
        y -= 1
    elif c == 'U' and x-1 >= 1:
        x -= 1
    elif c == 'D'and x+1 <= 5:
        x += 1

for c in command:
    move(c)

print(x,y)





