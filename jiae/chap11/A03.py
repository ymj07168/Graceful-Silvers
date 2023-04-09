data = input()

def reverse_string1():
  
  zero = 0
  one = 0
  for i in data:
    if int(i) == 0:
      zero +=1 
    else:
      one += 1

  result = 0
  if zero > one:
    for i in range(len(data)):
      if data[i] == '1':
        if data[i] != data[i+1]: 
          result += 1
        data[i] == '0'
  else:
    for i in range(len(data)):
      if data[i] == '0':
        if data[i] != data[i+1]: 
          result += 1
        data[i] == '1'
        
  return result

def reverse_string2():
  count0 = 0  # 전부 0으로 바꾸는 경우
  count1 = 0  # 전부 1로 바꾸는 경우
  
  if data[0] == '1':
    count0 += 1
  else:
    count1 += 1
    
  for i in range(len(data)-1):
    if data[i] != data[i+1]:
      # 0에서 1로 바뀌는 경우
      if data[i+1] == '1':
        count0 += 1
      # 1에서 0으로 바뀌는 경우
      else:
        count1 += 1

  return min(count0, count1)

print(reverse_string2())