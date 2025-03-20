n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
import sys

max_val = -sys.maxsize
sub_max_val = -sys.maxsize

for i in a :
    if i >= max_val :
        max_val = i

a.remove(max_val)

for i in a :
    if i >= sub_max_val and i <= max_val :
        sub_max_val = i

print(max_val, sub_max_val)