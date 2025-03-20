n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
import sys

max_idx = n

for _ in range(n) :
    max_val = -sys.maxsize
    for idx, i in enumerate(a[:max_idx]) :
        if i > max_val :
            max_val = i
            max_idx = idx

    print(max_idx+1, end=' ') 

    if max_idx+1 == 1:
        break



