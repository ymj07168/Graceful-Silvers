from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(6)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 다음 출력 위해 역순으로 변경
print(queue) # 나중에 들어온 원소부터 출력