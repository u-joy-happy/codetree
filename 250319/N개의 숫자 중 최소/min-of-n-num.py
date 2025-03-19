n = int(input())
a = list(map(int, input().split()))

# Please write your code here.

import sys

min_val = sys.maxsize

cnt = 0

for i in a :
    if i < min_val :
        min_val = i
        cnt = 0

    if i == min_val :
        cnt += 1        

print(min_val, cnt, sep=' ')