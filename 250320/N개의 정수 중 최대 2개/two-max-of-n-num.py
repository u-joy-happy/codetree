n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
import sys

max_val = -sys.maxsize
max_idx = -1
sub_max_val = -sys.maxsize

for idx, i in enumerate(a) :
    if i >= max_val :
        max_val = i
        max_idx = idx

for idx, i in enumerate(a) :
    if idx == max_idx :
        continue
        
    if i >= sub_max_val and i <= max_val :
        sub_max_val = i

print(max_val, sub_max_val)