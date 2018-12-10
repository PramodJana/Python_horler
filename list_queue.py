from collections import deque
queue = deque(["Eric", "John", "Michael"])
print(queue)
print(queue.append("Terry"))
print(queue.append("Graham"))
print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue)
