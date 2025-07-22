N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
import sys
res = sys.maxsize

for i in range(N):
    for j in range(i+1, N):
        sum_val = sum(arr) - arr[i] - arr[j]
        res = min(abs(S - sum_val), res)

print(res)