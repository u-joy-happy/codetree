n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
import sys

max_val = -sys.maxsize
term = sys.maxsize
tmp_idx = -1

for idx, i in enumerate(a) :
    if i > max_val:
        max_val = i
        max_term = -sys.maxsize
        term = sys.maxsize
        tmp_idx = -1
    elif i > max_val - term:
        term = max_val - i
        tmp_idx = idx

print(max_val, a[tmp_idx], sep=' ')

