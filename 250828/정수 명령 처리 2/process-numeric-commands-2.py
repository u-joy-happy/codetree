N = int(input())
command = []
A = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        A.append(int(line[1]))
    else:
        A.append(0)

# Please write your code here.

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()
    
    def push(self, data):
        self.queue.append(data)
    
    def pop(self):
        if self.empty():
            raise Exception
        return self.queue.popleft()
    
    def size(self):
        return len(self.queue)
    
    def empty(self):
        return self.size() == 0
    
    def front(self):
        return self.queue[0]

queue = Queue()
for i in range(N):
    if command[i] == 'push':
        queue.push(A[i])
    elif command[i] == 'pop':
        print(queue.pop())
    elif command[i] == 'size':
        print(queue.size())
    elif command[i] == 'empty':
        print(1 if queue.empty() else 0)
    elif command[i] == 'front':
        print(queue.front())
