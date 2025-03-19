import sys
arr = map(int, input().split())

max_val = -sys.maxsize

for a in arr :
    if a >= max_val :
        max_val = a

print(max_val)