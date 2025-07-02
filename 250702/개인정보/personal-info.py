n = 5
name = []
height = []
weight = []

for _ in range(n):
    n, h, w = input().split()
    name.append(n)
    height.append(int(h))
    weight.append(float(w))

# Please write your code here.

class Person:
    def __init__(self, name, height, weight) :
        self.name = name
        self.height = height
        self.weight = weight

pp = [ Person(name[i], height[i], weight[i]) for i in range(5)]

pp.sort(key=lambda x : x.name)

print('name')
for p in pp :
    print(p.name, p.height, p.weight)

print()
pp.sort(key=lambda x : -x.height)

print('height')
for p in pp :
    print(p.name, p.height, p.weight)
