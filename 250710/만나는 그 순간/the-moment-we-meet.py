n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

# Please write your code here.
import sys

a = [sys.maxsize] * (1000*1000)
b = [sys.maxsize] * (1000*1000)

cur, idx = 0, 0
for i in range(n) :
    for _ in range(t[i]):
        if d[i] == 'L':
            cur -= 1 
            a[idx] = cur
        else : 
            cur += 1 
            a[idx] = cur 
        idx += 1

cur, idx = 0, 0
for i in range(m) :
    for _ in range(t2[i]):
        if d2[i] == 'L':
            cur -= 1 
            b[idx] = cur
        else : 
            cur += 1 
            b[idx] = cur 
        idx += 1


for i in range(len(a)):
    if a[i] == sys.maxsize and b[i] == sys.maxsize or a[i] != b[i] and i == len(a)-1:
        print(-1)
        break
    if a[i] == b[i] :
        print(i+1)
        break
