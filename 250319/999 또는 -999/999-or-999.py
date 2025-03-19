import sys

arr = list(map(int, input().split()))

max_val = -sys.maxsize
min_val = sys.maxsize

for a in arr :
    if a == 999 or a == -999 :
        break
    
    if a > max_val :
        max_val = a
    if a < min_val :
        min_val = a


print(max_val, min_val, sep=' ')