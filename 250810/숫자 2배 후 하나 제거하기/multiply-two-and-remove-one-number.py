n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
import sys
min_val = sys.maxsize
for i in range(n):
    arr[i] *= 2
    for j in range(n):
        if i == j :
            continue
        tmp_arr = [ item for k, item in enumerate(arr) if k != j ]
        diff_sum = 0
        for k in range(n - 2):
            diff_sum += abs(tmp_arr[k + 1] - tmp_arr[k])
        min_val = min(min_val, diff_sum)    
    arr[i] //= 2

print(min_val)