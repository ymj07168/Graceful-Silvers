# 만들 수 없는 금액

def make_money1():
  n = int(input())
  data = list(map(int, input().split()))
  data = sorted(data, reverse=True)
  a = []

  for i in range(1, data[-1]+1):
    a.append(i)
    
  min_value = 0
  for i in a:
    if i in data:
      a.remove(i)
    else:
      temp = i
      for coin in data:
        if temp - coin < 0:
          continue
        else:
          temp -= coin
      if temp != 0:
        min_value = i
        break

  print(min_value)
  
make_money1()