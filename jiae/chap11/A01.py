# 모험가 길드

n = int(input())
a = list(map(int, input().split()))
a = sorted(a)  # 오름차순 정렬

def create_guild1():
  
  result = 0  # 총 그룹의 수
  i = 0       # 인덱스

  while i < len(a):      # 공포도 낮은 것부터 확인
    if i+a[i] < len(a):  # 현재 모험가 인덱스와 해당 모험가의 공포도 합이 배열 길이보다 작은지 확인
      result += 1        # 총 그룹의 수 증가시키기
      i += a[i]          # 포함된 모험가 다음의 사람부터 길드 생성하도록 인덱스 증가
    else:
      break
    
  return result

def create_guild2():
  
  result = 0  # 총 그룹의 수
  count = 0   # 현재 그룹에 포함된 모험가의 수
  
  for i in a:
    count += 1      # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i:  # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
      result += 1   # 총 그룹의 수 증가시키기
      count = 0     # 현재 그룹에 포함된 모험가의 수 초기화

  return result

print(create_guild2())
    