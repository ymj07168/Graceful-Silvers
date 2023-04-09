# 볼링공 고르기

def choose_ball1():
  
  result = 0
  for i in range(len(data)):
    p1 = data[i]
    for j in range(i+1, len(data)):
      p2 = data[j]
      if p1 != p2:
        result += 1
        
  print(result)
  
  
def choose_ball2():
  
  # 볼링공 개수 세기
  array = [0] * 11
  for i in data:
    array[i] += 1
  
  result = 0
  for i in range(1, m + 1):
    n -= array[i]
    result += array[i] * n

  print(result)
  
  
n, m = map(int, input().split())
data = list(map(int, input().split()))  
choose_ball2()