n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.

import sys 
min_val = sys.maxsize
res = -1

for i in range(n):
    # ext = 0
    max_x, max_y = 0, 0
    min_x, min_y = 40000, 40000
    for j in range(n):
        if i == j :
            continue
        if x[j] > max_x : max_x = x[j]
        if y[j] > max_y : max_y = y[j]
        if x[j] < min_x : min_x = x[j]
        if y[j] < min_y : min_y = y[j]
    nx = max_x - min_x
    ny = max_y - min_y
    ext = nx * ny
    if ext < min_val :
        min_val = ext
        res = i
print(min_val)