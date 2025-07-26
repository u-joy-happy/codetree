n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
import sys
min_val = sys.maxsize

for i in range(n):
    for j in range(i+1, n):
        diff = abs(x[i] - x[j]) ** 2  + abs(y[i] - y[j]) ** 2
        min_val = min(min_val, diff)

print(min_val)