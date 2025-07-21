n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
import sys
min_val = sys.maxsize
sum_val = 0

for i in range(1, n):
    for j in range(1, n):
        if j == i :
            continue
        elif j-1 == i :
            diff = abs(x[j-2] - x[j]) + abs(y[j-2] - y[j])
        else :
            diff = abs(x[j-1] - x[j]) + abs(y[j-1] - y[j])
        sum_val += diff
    min_val = min(sum_val, min_val)
    sum_val = 0

print(min_val)