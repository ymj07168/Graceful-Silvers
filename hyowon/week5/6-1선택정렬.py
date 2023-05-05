# 선택정렬
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i
    # 남은 원소 중 가장 작은 원소의 인덱스 찾기
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    # 스와프 : 두 원소 위치 변경
    array[i], array[min_index] = array[min_index], array[i]

print(array)