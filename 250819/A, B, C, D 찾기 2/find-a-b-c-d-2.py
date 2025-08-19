nums = list(map(int, input().split()))

# Please write your code here.

nums.sort()

a = nums[0]
for b in range(a, 41):
    for c in range(b, 41):
        for d in range(c, 41):
            new_num = [a, b, c, d, a+b, b+c, c+d, d+a, a+c, b+d, a+b+c, a+b+d, a+c+d, b+c+d, a+b+c+d]
            new_num.sort()
            if nums == new_num :
                print(a, b, c, d)