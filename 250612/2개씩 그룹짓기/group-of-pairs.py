n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.

nums.sort()
max_val = 0

for i in range(n):
    sum_val = nums[i] + nums[2*n-1-i]
    if max_val < sum_val :
        max_val = sum_val

print(max_val) 
