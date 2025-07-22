n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
import sys
max_val = -sys.maxsize

for i in range(n-k+1):
    max_val = max(max_val, sum(arr[i:i+k]))

print(max_val)

