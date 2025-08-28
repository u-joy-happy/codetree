str = input()

# Please write your code here.

class Stack :
    def __init__(self):
        self.stack = []
    
    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        return self.stack.pop()
    
    def size(self):
        return len(self.stack)
    
    def empty(self):
        return self.size() == 0

stack = Stack()
flag = True
for n in str :
    if n == '(' :
        stack.push('(')
    else :
        if stack.empty() :
            flag = False
            break 
        stack.pop()

if stack.empty() and flag :
    print('Yes')
else :
    print('No')