n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
import sys

new_arr = []
max_val = -1

for idx, i in enumerate(nums) :
    if i >= max_val and i not in nums[0:idx] + nums[idx+1:] :
        max_val = i

print(max_val)