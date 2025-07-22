n = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.
import sys
max_val = -sys.maxsize

for i in range(n):
    for j in range(i+1, n):
        if abs(i - j) == 1 :
            continue
        max_val = max(max_val, numbers[i]+numbers[j])

print(max_val)