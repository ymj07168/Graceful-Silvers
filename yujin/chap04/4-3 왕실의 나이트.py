here = input()

# 입력받은 현재 위치 인덱스 값으로 변환
# a 아스키 97
col = ord(here[0]) - 97
row = int(here[1]) - 1

count = 0

# row 2 + col 1 / col 2 + row 1 조합
# 이번에는 4-1에서 책에서 좌표값 이용했으니 적용해보겠음
move_list = [(-2, -1), (-2, 1),
             (2, -1), (2, 1),
             (1, -2), (1, 2),
             (-1, 2), (-1, -2)]

for move in move_list:
    r = row + move[0]
    c = col + move[1]
    if r> -1 and r < 8 and c>-1 and c < 8:
        count += 1

print(count)