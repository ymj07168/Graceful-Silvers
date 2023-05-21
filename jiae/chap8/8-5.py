# 1로 만들기

# 정수 x를 입력받기
x = int(input())

# 앞서 계산된 결과를 저장하기 위한 dp 테이블 초기화
d = [0] * 30001
d[1] = 0
d[2] = 1
d[3] = 1
d[4] = 2
d[5] = 1

# bottom-up 방식을 이용한 dp 진행
for i in range(6, x + 1):
  tmp = []
  tmp.append(d[i-1])  # 현재 수에서 1을 빼는 경우
  if i % 2 == 0:  # 현재 수가 2로 나누어 떨어지는 경우
    tmp.append(d[i // 2])
  if i % 3 == 0:  # 현재 수가 3로 나누어 떨어지는 경우
    tmp.append(d[i // 3])
  if i % 5 == 0:  # 현재 수가 5로 나누어 떨어지는 경우
    tmp.append(d[i // 5])
  d[i] = min(tmp) + 1

print(d[x])