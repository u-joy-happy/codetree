n = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.
import sys
max_val = -sys.maxsize

for i in range(n):
    for j in range(i+2, n):
        max_val = max(max_val, numbers[i]+numbers[j])

print(max_val)