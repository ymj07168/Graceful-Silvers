now = input()

  
def knight_move1():
  x = ord(now[0])- 96
  y = int(now[1])

  # 체스값 범위, 이동할 수 있는 8가지 방향 정의
  n = 8
  dx = [-2, -2, 2, 2, -1, -1, 1, 1]
  dy = [-1, 1, -1, 1, -2, 2, -2, 2]

  count = 0
  for i in range(8):
    # 이동하고자 하는 위치 확인
    nx = x + dx[i]
    ny = y + dy[i]
    # x, y값이 범위 밖이면 다음 이동 위치 확인
    if nx < 1 or ny < 1 or nx > n or ny > n:
      continue
    count += 1

  print(count)
  
def knight_move2():
  # 현재 나이트의 위치
  row = int(now[1])
  column = int(ord(now[0])) - int(ord('a')) + 1
  
  # 나이트가 이동할 수 있는 8가지 방향 정의
  steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
  
  # 8가지 방향에 대해 각 위치로 이동이 가능한지 확인
  count = 0
  for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
      count += 1
  
  print(count)
  
knight_move2()