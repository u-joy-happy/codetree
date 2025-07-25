N = int(input())
command = []
A = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] in ["push_front", "push_back"]:
        A.append(int(line[1]))
    else:
        A.append(0)

# Please write your code here.

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoubleLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.node_num = 0
    
    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head != None :
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.node_num += 1

    def push_back(self, data):
        new_node = Node(data)
        new_node.prev = self.tail
        if self.tail != None :
            self.tail.next = new_node
            self.tail = new_node
        else :
            self.head = new_node
            self.tail = new_node
        self.node_num += 1
    
    def pop_front(self):
        rm_data = self.head
        if self.head == None :
            pass
        elif self.head.next == None :
            self.head = None
            self.tail = None
            self.node_num -= 1
            return rm_data.data
        else :
            rm_data = self.head
            self.head = self.head.next
            self.head.prev = None
            rm_data.next = None
            self.node_num -= 1
            return rm_data.data

    def pop_back(self):
        rm_data = self.tail
        if self.tail == None :
            pass
        elif self.tail.prev == None:
            self.tail = None
            self.head = None
            self.node_num -= 1
            return rm_data.data
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            rm_data.prev = None 
            self.node_num -= 1
            return rm_data.data
    
    def size(self):
        return self.node_num
    
    def empty(self):
        return 1 if self.node_num == 0 else 0
    
    def front(self):
        return self.head.data
    
    def back(self):
        return self.tail.data

dll = DoubleLinkedList()

for i in range(N):
    if command[i] == 'push_front':
        dll.push_front(A[i])
    elif command[i] == 'push_back':
        dll.push_back(A[i])
    elif command[i] == 'pop_front':
        print(dll.pop_front())
    elif command[i] == 'pop_back':
        print(dll.pop_back())
    elif command[i] == 'size':
        print(dll.size())
    elif command[i] == 'empty':
        print(dll.empty())
    elif command[i] == 'front':
        print(dll.front())
    elif command[i] == 'back':
        print(dll.back())