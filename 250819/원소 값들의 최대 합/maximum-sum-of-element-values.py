n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# Please write your code here.

max_val = 0

for i in range(n):
    idx = i
    sum_val = 0
    for j in range(m):
        sum_val += arr[idx]
        idx = arr[idx] -1
    max_val = max(max_val, sum_val)
print(max_val)