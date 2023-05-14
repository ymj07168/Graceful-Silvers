# 부품 찾기(이진 탐색)

def binary_search(arr, target, start, end):
  if start > end:
    return None
  
  mid = (start + end) // 2  # 중간값 설정

  if arr[mid] == target:  # 중간값이 찾고싶은 값과 동일한 경우
    return mid
  
  elif arr[mid] > target: # 찾고싶은 값이 중간값보다 작은 경우
    return binary_search(arr, target, start, mid - 1)  # 왼쪽 탐색
    
  else: # 찾고싶은 값이 중간값보다 큰 경우
    return binary_search(arr, target, mid + 1, end)  # 오른쪽 탐색

n = int(input())
n_arr = list(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))

n_arr = sorted(n_arr)

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in m_arr:
  if binary_search(n_arr, i, 0, n - 1):
    print("yes", end=' ')
  else:
    print("no", end=' ')