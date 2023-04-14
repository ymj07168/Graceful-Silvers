N = int(input()) -1 # 인덱스로 접근할거여서
move_plan = map(str, input().split())

here = [0, 0]
# 문제에서 시작은 1,1이나 우리는 인덱스로 접근할 것이므로 0,0
# 맨 마지막에 +1씩 해주면 됨

for move in move_plan:
    if move == 'L':
        # 왼#
        if here[1]-1 < 0:
            pass
        else:
            here[1]-=1
    elif move == 'R':
        # 오른쪽
        if here[1] + 1 > N:
            pass
        else:
            here[1] += 1
    elif move == 'U':
        # 위
        if here[0] - 1 < 0:
            pass
        else:
            here[0] -= 1
    elif move == 'D':
        # 아래
        if here[0]+1 > N:
            pass
        else:
            here[0]+=1

print(here[0]+1, here[1]+1)