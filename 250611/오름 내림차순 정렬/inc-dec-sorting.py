n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.

nums.sort()
for item in nums : print(item, end=' ')
print()
nums.sort(reverse=True)
for item in nums : print(item, end=' ')
