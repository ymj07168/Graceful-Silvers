# 3 숫자 카드 게임
# 입력 조건: 첫줄 N행 M열 공백 기준 자연수, 둘째 줄 N개의 줄에 걸쳐 카드 적힌 숫자
# 출력 조건: 게임 룰 맞게 선택 카드 적힌 숫자 출력

# 입력 받기
N, M = map(int, input().split())
card_list = []
for i in range(N):
    card_list.append(list(map(int, input().split())))
#print(card_list)
# 각 행별로 가장 작은 수 체크
min_list = []
for i in range(N):
    min_list.append(min(card_list[i]))
#print(min_list)
# 작은 수들 중 가장 큰 수
print(max(min_list))

