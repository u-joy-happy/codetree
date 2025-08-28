n, k = map(int, input().split())

# Please write your code here.

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()
    
    def push(self, data):
        self.queue.append(data)
    
    def pop(self):
        if self.empty() :
            raise Exception
        return self.queue.popleft()
    
    def size(self):
        return len(self.queue)
    
    def empty(self):
        return self.size() == 0
    
    def front(self):
        return self.queue[0]

queue = Queue()

for i in range(n):
    queue.push(i+1)

for i in range(n):
    for j in range(k-1):
        queue.push(queue.front())
        queue.pop()
    print(queue.pop(), end=' ')