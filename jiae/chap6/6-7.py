# 위에서 아래로

N = int(input())
array = []
for i in range(N):
  array.append(int(input()))

def quick_sort(array):
  if len(array) <= 1:
    return array
  
  pivot = array[0]
  tail = array[1:]
  
  left_side = [x for x in tail if x <= pivot] # 피봇보다 작은 원소만 저장
  right_side = [x for x in tail if x > pivot] # 피봇보다 큰 원소만 저장
  
  return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))