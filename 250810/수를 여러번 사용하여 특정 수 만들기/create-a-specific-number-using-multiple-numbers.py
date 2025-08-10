A, B, C = map(int, input().split())

# Please write your code here.

max_val = 0
for i in range(1001):
    for j in range(1001):
        sum_val = (A * i) + (B * j)
        if sum_val <= C :
            max_val = max(max_val, sum_val)

print(max_val)