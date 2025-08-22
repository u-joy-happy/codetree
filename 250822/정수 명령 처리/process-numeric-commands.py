N = int(input())
command = []
value = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        value.append(int(line[1]))
    else:
        value.append(0)

# Please write your code here.

class Stack :
    def __init__(self):
        self.s = []

    def push(self, data):
        self.s.append(data)
    
    def pop(self):
        if self.empty() :
            raise Exception()
        return self.s.pop()
    
    def size(self):
        return len(self.s)
    
    def empty(self):
        return True if self.size() == 0 else False

    def top(self):
        return self.s[-1]
    
stack = Stack()

for i in range(N):
    if command[i] == 'push':
        stack.push(value[i])
    elif command[i] == 'pop':
        print(stack.pop())
    elif command[i] == 'size':
        print(stack.size())
    elif command[i] == 'empty':
        print(1 if stack.empty() else 0)
    elif command[i] == 'top':
        print(stack.top())

