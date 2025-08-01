X, Y = map(int, input().split())

# Please write your code here.

max_val = 0
for i in range(X, Y+1):
    sum_val = 0
    while i > 0 :
        sum_val += (i % 10)
        i //= 10
    max_val = max(max_val, sum_val)

print(max_val)