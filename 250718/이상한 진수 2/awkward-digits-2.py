a = input()

# Please write your code here.
import sys

def to_decimal(num):
    res = 0
    for n in num:
        res = (res * 2) + int(n)
    return res

max_int = -sys.maxsize
for i in range(len(a)) :
    list_val = list(a)
    if list_val[i] == '0' :
        list_val[i] = '1'
    else :
        list_val[i] = '0'
    max_int = max(max_int, to_decimal(''.join(list_val)))

print(max_int)