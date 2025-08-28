n = int(input())

# Please write your code here.
from collections import deque

dq = deque()

for i in range(n):
    dq.append(i+1)

for i in range(n-1):
    dq.popleft()
    dq.append(dq.popleft())

print(dq[0])