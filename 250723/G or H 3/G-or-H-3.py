n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# Please write your code here.

import sys
max_val = -sys.maxsize
arr = [0] * max(x)

for i in range(n):
    arr[x[i]-1] = c[i]

for i in range(len(arr)-k):
    sum_val = 0
    for j in range(i, i+k+1):
        if arr[j] == 'G' :
            sum_val += 1
        elif arr[j] == 'H' :
            sum_val += 2
    max_val = max(max_val, sum_val)

print(max_val)