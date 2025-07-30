n, m = map(int, input().split())
s = input()

commands = []
for _ in range(m):
    cmd = input().split()
    if len(cmd) == 1:
        commands.append((cmd[0],))
    else:
        commands.append((cmd[0], cmd[1]))

# Please write your code here.

class Node:
    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DoubleLinkedList:
    def __init__(self):
        self.point = Node(-1)
        self.head = self.point
        self.tail = self.point
    
    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    
    def push_back(self, data):
        if self.begin() == self.end() :
            self.push_front(data)
        else :
            new_node = Node(data)
            new_node.prev = self.tail.prev
            new_node.next = self.tail
            self.tail.prev.next = new_node
            self.tail.prev = new_node

    def erase(self, node):
        next_node = node.next
        if node == self.begin() :
            next_node.prev = None
            node.next = None
            self.head = next_node
        else :
            node.prev.next = next_node
            next_node.prev = node.prev
            node.prev = None
            node.next = None
        return next_node
    
    def insert(self, node, data):
        if node == self.begin() :
            self.push_front(data)
        elif node == self.end() :
            self.push_back(data)
        else :
            new_node = Node(data)
            new_node.prev = node.prev
            node.prev.next = new_node
            new_node.next = node
            node.prev = new_node

    def begin(self):
        return self.head
    
    def end(self):
        return self.tail

dll = DoubleLinkedList()
for item in s :
    dll.push_back(item)

itl = dll.tail
for i in range(m):
    cmd = commands[i][0]
    if cmd == 'L':
        if itl != dll.begin():
            itl = itl.prev
    elif cmd == 'R':
        if itl != dll.end():
            itl = itl.next
    elif cmd == 'D':
        if itl != dll.end():
            itl = dll.erase(itl)
    elif cmd == 'P':
        dll.insert(itl, commands[i][1])

cur = dll.head
while cur.next != None :
    print(cur.data, end='')
    cur = cur.next

