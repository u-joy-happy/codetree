n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
import sys

res = -1
max_val = -sys.maxsize

def sum_if(a, b, c):
    if a == 0 and b == 0 and c == 0 :
        return True
    elif a % 10 + b % 10 + c % 10 >= 10:
        return False
    return sum_if(a // 10, b // 10, c //10)


for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            a, b, c = arr[i], arr[j], arr[k]
            if sum_if(a, b, c) :
                max_val = max(max_val, a+b+c)

print(max(res, max_val))