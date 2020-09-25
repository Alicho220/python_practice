# first in first out.. FIFO concept..
# on like  a que in the real world..
# import a deque object
# it deals its dealing from the left

from collections import deque

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()

print(queue)



