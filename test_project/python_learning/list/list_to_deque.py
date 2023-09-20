from collections import deque

queue = deque(["Erix", "Join", "Michael"])

# 添加到对尾
queue.append("Terry")
queue.append("graham")

# 从对头删除。等价于queue.pop(0)
print(queue.popleft())
# 从对尾删除
print(queue.pop())

# 添加到对头
queue.appendleft("Zhangfei")
print(queue)

