n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

import sys

max_val = -sys.maxsize

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def check(i, j, k, l):
    if i == k :
        return abs(l - j) >= 3
    return True

for i in range(n):
    for j in range(n):
        for k in range(i, n):
            for l in range(j, n):
                if check(i, j, k, l) and in_range(i, j+2) and in_range(k, l+2):
                    max_val = max(max_val, sum(arr[i][j:j+3]+arr[k][l:l+3]))

print(max_val)
