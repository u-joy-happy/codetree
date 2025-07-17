n = int(input())
A = list(map(int, input().split()))

# Please write your code here.

import sys

min_size = sys.maxsize

for i in range(n):
    sum_val = 0
    for j in range(n):
        if j == i :
            continue
        sum_val = sum_val + A[j]*abs(j-i)
    if sum_val < min_size :
        min_size = sum_val

print(min_size)