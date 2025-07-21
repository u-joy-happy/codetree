n = int(input())
a = [int(input()) for _ in range(n)]

# Please write your code here.
import sys
sum_val = 0
min_val = sys.maxsize

for i in range(n):
    for j in range(n):
        idx = (n+j-i) % n 
        sum_val += a[idx] * j
    min_val = min(sum_val, min_val)
    sum_val = 0

print(min_val)